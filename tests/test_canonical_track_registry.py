from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_curriculum.taxonomy import (  # noqa: E402
    UnknownTrackIdError,
    build_export,
    compute_registry_hash,
    digital_rc_package_dirs,
    load_alias_map,
    load_registry,
    reset_resolver_cache,
    resolve_track_id,
    validate_registry,
)


@pytest.fixture(autouse=True)
def _reset_cache():
    reset_resolver_cache()
    yield
    reset_resolver_cache()


def test_exactly_eighteen_tracks():
    reg = load_registry()
    assert reg["track_count"] == 18
    assert len(reg["tracks"]) == 18
    assert len(validate_registry()) == 0


def test_uuid_uniqueness():
    uuids = [t["stable_uuid"] for t in load_registry()["tracks"]]
    assert len(uuids) == 18
    assert len(set(uuids)) == 18


def test_track_id_uniqueness():
    ids = [t["track_id"] for t in load_registry()["tracks"]]
    assert len(ids) == 18
    assert len(set(ids)) == 18


def test_alias_uniqueness():
    seen = {}
    for t in load_registry()["tracks"]:
        for a in t["historical_aliases"]:
            assert a not in seen, f"duplicate alias {a}"
            seen[a] = t["track_id"]
    amap = load_alias_map()
    for entry in amap["aliases"]:
        a = entry["alias"]
        assert seen[a] == entry["canonical_track_id"]


def test_unknown_id_rejection():
    with pytest.raises(UnknownTrackIdError):
        resolve_track_id("NOT_A_REAL_TRACK")
    with pytest.raises(UnknownTrackIdError):
        resolve_track_id("GENERAL_IT")
    with pytest.raises(UnknownTrackIdError):
        resolve_track_id("general_it")
    with pytest.raises(UnknownTrackIdError):
        resolve_track_id("networking")  # similar title, not aliased
    with pytest.raises(UnknownTrackIdError):
        resolve_track_id("")


def test_known_aliases_resolve():
    assert resolve_track_id("DIGITAL_CONFIDENCE") == "DIGITAL_CONFIDENCE"
    assert resolve_track_id("WAIKE_COURSE_DIGITAL_CONFIDENCE") == "DIGITAL_CONFIDENCE"
    assert resolve_track_id("digital_confidence") == "DIGITAL_CONFIDENCE"
    assert resolve_track_id("COMPUTER_NETWORKING") == "NETWORKING_INFRA"
    assert resolve_track_id("CYBERSECURITY") == "CYBER_SOC"
    assert resolve_track_id("cybersecurity") == "CYBER_SOC"


def test_deterministic_export_hash_stability():
    h1 = compute_registry_hash()
    h2 = compute_registry_hash()
    assert h1 == h2
    assert len(h1) == 64
    export_a = build_export(source_commit_sha="deadbeef")
    export_b = build_export(source_commit_sha="cafebabe")
    # commit sha differs but registry_hash is content-stable
    assert export_a["registry_hash"] == export_b["registry_hash"] == h1
    assert export_a["source_commit_sha"] != export_b["source_commit_sha"]


def test_package_mapping_not_alias_when_multi_track():
    reg = load_registry()
    multi = [
        m for m in reg["package_mappings"] if len(m["covers_track_ids"]) != 1
    ]
    assert any(m["package_id"] == "GENERAL_IT" for m in multi)
    alias_keys = {
        a for t in reg["tracks"] for a in t["historical_aliases"]
    }
    for m in multi:
        assert m["package_id"] not in alias_keys
    # GENERAL_IT must not resolve; HARDWARE_ENGINEERING resolves as track_id only
    with pytest.raises(UnknownTrackIdError):
        resolve_track_id("GENERAL_IT")
    assert resolve_track_id("HARDWARE_ENGINEERING") == "HARDWARE_ENGINEERING"


def test_digital_rc_disk_count_method():
    pkgs = digital_rc_package_dirs(ROOT)
    assert len(pkgs) == 16
    assert "GENERAL_IT" in pkgs
    assert "COMPUTER_NETWORKING" in pkgs


def test_required_record_fields_present():
    required = {
        "stable_uuid",
        "track_id",
        "title",
        "historical_aliases",
        "academy_id",
        "extension_class",
        "authoritative_source_paths",
        "prerequisites",
        "content_maturity",
        "latest_compatible_package_version",
        "deprecation",
    }
    for t in load_registry()["tracks"]:
        assert required <= set(t)
        assert "outcome_refs" in t or "outcomes" in t
        assert t["latest_compatible_package_version"] is None or isinstance(
            t["latest_compatible_package_version"], str
        )


def test_export_artifact_roundtrip_shape():
    export = build_export(source_commit_sha="testsha")
    assert export["schema_version"]
    assert export["compatibility_version"]
    assert export["source_commit_sha"] == "testsha"
    assert export["alias_map"]["schema"].startswith("waike.taxonomy.track_alias_map")
    assert export["package_mappings"]
    # JSON round-trip stable for hash payload
    raw = json.dumps(export, sort_keys=True)
    assert json.loads(raw)["registry_hash"] == export["registry_hash"]
