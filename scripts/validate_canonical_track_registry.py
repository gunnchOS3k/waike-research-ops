#!/usr/bin/env python3
"""Validate canonical track registry + alias map (fail closed)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_curriculum.taxonomy import (  # noqa: E402
    UnknownTrackIdError,
    resolve_track_id,
    reset_resolver_cache,
    validate_registry,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--resolve",
        action="append",
        default=[],
        help="Attempt resolve_track_id on a raw id (may be repeated)",
    )
    parser.add_argument(
        "--expect-unknown",
        action="append",
        default=[],
        help="Assert that a raw id is rejected (may be repeated)",
    )
    args = parser.parse_args()

    errors = validate_registry()
    if errors:
        print("INVALID")
        for err in errors:
            print(f"  - {err}")
        return 1

    reset_resolver_cache()
    for raw in args.resolve:
        try:
            print(f"RESOLVE {raw!r} -> {resolve_track_id(raw)}")
        except UnknownTrackIdError as exc:
            print(f"FAIL resolve {raw!r}: {exc}", file=sys.stderr)
            return 1

    for raw in args.expect_unknown:
        try:
            got = resolve_track_id(raw)
            print(f"FAIL expected unknown {raw!r} but got {got}", file=sys.stderr)
            return 1
        except UnknownTrackIdError:
            print(f"REJECT {raw!r} (fail-closed OK)")

    print("OK: canonical track registry valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
