"""Canonical 18-track taxonomy contract: load, resolve, hash, export helpers."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "curriculum" / "taxonomy" / "canonical_track_registry.v1.json"
ALIAS_MAP_PATH = ROOT / "curriculum" / "taxonomy" / "track_alias_map.v1.json"
EXPORT_PATH = ROOT / "artifacts" / "taxonomy" / "CANONICAL_TRACK_REGISTRY.export.json"

SCHEMA_VERSION = "1.0.0"
COMPATIBILITY_VERSION = "waike.taxonomy.consumer.v1"


class UnknownTrackIdError(ValueError):
    """Raised when resolve_track_id cannot map a raw identifier fail-closed."""


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry(path: Path | None = None) -> dict[str, Any]:
    return _load_json(path or REGISTRY_PATH)


def load_alias_map(path: Path | None = None) -> dict[str, Any]:
    return _load_json(path or ALIAS_MAP_PATH)


def canonical_tracks(registry: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    reg = registry if registry is not None else load_registry()
    return list(reg["tracks"])


def track_ids(registry: dict[str, Any] | None = None) -> list[str]:
    return [t["track_id"] for t in canonical_tracks(registry)]


def build_resolver_index(
    registry: dict[str, Any] | None = None,
    alias_map: dict[str, Any] | None = None,
) -> dict[str, str]:
    """Exact alias/track_id -> canonical track_id. Fail-closed; no fuzzy keys."""
    reg = registry if registry is not None else load_registry()
    amap = alias_map if alias_map is not None else load_alias_map()
    index: dict[str, str] = {}

    for track in reg["tracks"]:
        tid = track["track_id"]
        if tid in index and index[tid] != tid:
            raise ValueError(f"track_id collision on {tid}")
        index[tid] = tid
        for alias in track.get("historical_aliases") or []:
            if alias in index and index[alias] != tid:
                raise ValueError(f"alias collision: {alias} -> {index[alias]} and {tid}")
            index[alias] = tid

    for entry in amap.get("aliases") or []:
        alias = entry["alias"]
        tid = entry["canonical_track_id"]
        if alias in index and index[alias] != tid:
            raise ValueError(f"alias map collision: {alias}")
        index[alias] = tid

    # Multi-track package IDs must never appear as historical aliases.
    # They may share a string with a canonical track_id (e.g. HARDWARE_ENGINEERING);
    # that track_id resolution is intentional and is not an alias claim.
    alias_keys = set()
    for track in reg["tracks"]:
        alias_keys.update(track.get("historical_aliases") or [])
    for entry in amap.get("aliases") or []:
        alias_keys.add(entry["alias"])
    for mapping in reg.get("package_mappings") or []:
        covers = mapping.get("covers_track_ids") or []
        if len(covers) != 1:
            pid = mapping["package_id"]
            if pid in alias_keys:
                raise ValueError(
                    f"multi-track package_id {pid} must not appear in historical aliases"
                )

    return index


_RESOLVER_INDEX: dict[str, str] | None = None


def _index() -> dict[str, str]:
    global _RESOLVER_INDEX
    if _RESOLVER_INDEX is None:
        _RESOLVER_INDEX = build_resolver_index()
    return _RESOLVER_INDEX


def reset_resolver_cache() -> None:
    global _RESOLVER_INDEX
    _RESOLVER_INDEX = None


def resolve_track_id(raw: str) -> str:
    """Map raw identifier to canonical track_id. Exact match only; fail closed."""
    if raw is None:
        raise UnknownTrackIdError("track id is required")
    key = str(raw).strip()
    if not key:
        raise UnknownTrackIdError("track id is empty")
    index = _index()
    if key not in index:
        raise UnknownTrackIdError(f"unknown track id: {raw!r}")
    return index[key]


def canonical_json_bytes(obj: Any) -> bytes:
    """Deterministic JSON encoding for hashing (sorted keys, compact separators)."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )


def registry_content_for_hash(registry: dict[str, Any] | None = None) -> dict[str, Any]:
    """Subset hashed for registry_hash: tracks + package_mappings only."""
    reg = registry if registry is not None else load_registry()
    return {
        "schema": reg["schema"],
        "schema_version": reg["schema_version"],
        "tracks": reg["tracks"],
        "package_mappings": reg.get("package_mappings") or [],
    }


def compute_registry_hash(registry: dict[str, Any] | None = None) -> str:
    payload = registry_content_for_hash(registry)
    return hashlib.sha256(canonical_json_bytes(payload)).hexdigest()


def git_head_sha(repo_root: Path | None = None) -> str:
    root = repo_root or ROOT
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return "UNKNOWN"


def build_export(
    registry: dict[str, Any] | None = None,
    alias_map: dict[str, Any] | None = None,
    *,
    source_commit_sha: str | None = None,
) -> dict[str, Any]:
    reg = registry if registry is not None else load_registry()
    amap = alias_map if alias_map is not None else load_alias_map()
    sha = source_commit_sha if source_commit_sha is not None else git_head_sha()
    return {
        "schema": "waike.taxonomy.canonical_track_registry.export.v1",
        "schema_version": reg.get("schema_version", SCHEMA_VERSION),
        "compatibility_version": reg.get("compatibility_version", COMPATIBILITY_VERSION),
        "source_commit_sha": sha,
        "registry_hash": compute_registry_hash(reg),
        "track_count": len(reg["tracks"]),
        "tracks": reg["tracks"],
        "alias_map": amap,
        "package_mappings": reg.get("package_mappings") or [],
    }


def write_export(path: Path | None = None, **kwargs: Any) -> dict[str, Any]:
    export = build_export(**kwargs)
    out = path or EXPORT_PATH
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(export, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    return export


def validate_registry(
    registry: dict[str, Any] | None = None,
    alias_map: dict[str, Any] | None = None,
) -> list[str]:
    """Return list of validation errors (empty if valid)."""
    errors: list[str] = []
    reg = registry if registry is not None else load_registry()
    amap = alias_map if alias_map is not None else load_alias_map()
    tracks = reg.get("tracks") or []

    if len(tracks) != 18:
        errors.append(f"expected 18 tracks, found {len(tracks)}")

    ids = [t.get("track_id") for t in tracks]
    uuids = [t.get("stable_uuid") for t in tracks]
    if len(set(ids)) != len(ids):
        errors.append("duplicate track_id")
    if len(set(uuids)) != len(uuids):
        errors.append("duplicate stable_uuid")

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
    for t in tracks:
        missing = required - set(t)
        if missing:
            errors.append(f"{t.get('track_id')}: missing fields {sorted(missing)}")
        if "outcomes" not in t and "outcome_refs" not in t:
            errors.append(f"{t.get('track_id')}: need outcomes or outcome_refs")

    try:
        index = build_resolver_index(reg, amap)
    except ValueError as exc:
        errors.append(str(exc))
        return errors

    alias_seen: dict[str, str] = {}
    for t in tracks:
        for a in t.get("historical_aliases") or []:
            if a in alias_seen and alias_seen[a] != t["track_id"]:
                errors.append(f"alias collision {a}")
            alias_seen[a] = t["track_id"]

    for mapping in reg.get("package_mappings") or []:
        covers = mapping.get("covers_track_ids") or []
        pid = mapping.get("package_id")
        if len(covers) != 1 and pid in alias_seen:
            errors.append(f"multi-track package {pid} must not be an alias")
        # Package-only IDs (not equal to any track_id) must not resolve.
        if len(covers) != 1 and pid not in ids and pid in index:
            errors.append(f"multi-track package {pid} resolves unexpectedly")

    return errors


def digital_rc_package_dirs(repo_root: Path | None = None) -> list[str]:
    """Exact disk count method: child dirs of curriculum/digital_rc that exist."""
    base = (repo_root or ROOT) / "curriculum" / "digital_rc"
    return sorted(p.name for p in base.iterdir() if p.is_dir())
