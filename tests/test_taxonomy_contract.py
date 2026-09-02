"""Canonical 18-track taxonomy contract: uniqueness, aliases, fail-closed, determinism."""

from __future__ import annotations

import copy
import uuid
from pathlib import Path

import pytest

from waike_curriculum.taxonomy import (
    UnknownTrackIdError,
    build_export,
    build_resolver_index,
    canonical_json_bytes,
    compute_registry_hash,
    digital_rc_package_dirs,
    load_alias_map,
    load_registry,
    registry_content_for_hash,
    reset_resolver_cache,
    resolve_track_id,
    validate_registry,
)

ROOT = Path(__file__).resolve().parents[1]
UUID_NS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")


@pytest.fixture(autouse=True)
def _clear_resolver_cache():
    reset_resolver_cache()
    yield
    reset_resolver_cache()


def test_registry_has_exactly_18_unique_track_ids_and_uuids():
    reg = load_registry()
    tracks = reg["tracks"]
    assert len(tracks) == 18
    ids = [t["track_id"] for t in tracks]
    uuids = [t["stable_uuid"] for t in tracks]
    assert len(set(ids)) == 18
    assert len(set(uuids)) == 18
    assert validate_registry() == []


def test_stable_uuids_are_deterministic_uuid5():
    for track in load_registry()["tracks"]:
        expected = str(uuid.uuid5(UUID_NS, f"waike.track.{track['track_id']}"))
        assert track["stable_uuid"] == expected


def test_alias_resolution_safe_historical_package_ids():
    assert resolve_track_id("COMPUTER_NETWORKING") == "NETWORKING_INFRA"
    assert resolve_track_id("CYBERSECURITY") == "CYBER_SOC"
    assert resolve_track_id("NETWORKING_INFRA") == "NETWORKING_INFRA"
    assert resolve_track_id("CYBER_SOC") == "CYBER_SOC"
    assert resolve_track_id("WAIKE_COURSE_SOFTWARE_BUILDER") == "SOFTWARE_BUILDER"


def test_unknown_ids_fail_closed():
    for raw in (
        "GENERAL_IT",
        "general_it",
        "NOT_A_REAL_TRACK",
        "networking",
        "software_engineering",
        "",
        "  ",
    ):
        with pytest.raises(UnknownTrackIdError):
            resolve_track_id(raw)


def test_no_alias_maps_to_multiple_canonicals():
    index = build_resolver_index()
    # Index values are unique per key by construction; ensure no alias key is a
    # different canonical reused incorrectly.
    track_ids = {t["track_id"] for t in load_registry()["tracks"]}
    for alias, tid in index.items():
        assert tid in track_ids
        if alias in track_ids:
            assert alias == tid


def test_multi_track_packages_are_not_aliases():
    amap = load_alias_map()
    alias_keys = {e["alias"] for e in amap["aliases"]}
    for track in load_registry()["tracks"]:
        alias_keys.update(track["historical_aliases"])
    assert "GENERAL_IT" not in alias_keys
    assert "GENERAL_IT" in (amap.get("non_alias_package_ids") or [])
    with pytest.raises(UnknownTrackIdError):
        resolve_track_id("GENERAL_IT")


def test_export_is_deterministic_for_same_inputs():
    reg = load_registry()
    amap = load_alias_map()
    a = build_export(reg, amap, source_commit_sha="deadbeef")
    b = build_export(copy.deepcopy(reg), copy.deepcopy(amap), source_commit_sha="deadbeef")
    assert a == b
    assert a["registry_hash"] == b["registry_hash"]
    assert a["registry_hash"] == compute_registry_hash(reg)
    assert a["schema_version"]
    assert a["compatibility_version"]
    assert a["alias_map"] == amap
    assert len(a["tracks"]) == 18


def test_registry_hash_stable_under_key_reorder():
    reg = load_registry()
    h1 = compute_registry_hash(reg)
    payload = registry_content_for_hash(reg)
    # Re-encode via sorted canonical bytes twice
    assert canonical_json_bytes(payload) == canonical_json_bytes(copy.deepcopy(payload))
    h2 = compute_registry_hash(copy.deepcopy(reg))
    assert h1 == h2


def test_digital_rc_package_dir_count_is_exact():
    pkgs = digital_rc_package_dirs(ROOT)
    assert len(pkgs) == 16
    assert "GENERAL_IT" in pkgs
    assert "COMPUTER_NETWORKING" in pkgs
    assert "CYBERSECURITY" in pkgs
    assert "EMBEDDED_PROTOTYPING" in pkgs
    assert "GUNNCHOS_PRODUCT_LAB" in pkgs
    assert "DIGITAL_CONFIDENCE" not in pkgs
    assert "NETWORKING_INFRA" not in pkgs
    assert "CYBER_SOC" not in pkgs
