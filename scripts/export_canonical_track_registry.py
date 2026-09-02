#!/usr/bin/env python3
"""Export consumer artifact artifacts/taxonomy/CANONICAL_TRACK_REGISTRY.export.json."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_curriculum.taxonomy import (  # noqa: E402
    EXPORT_PATH,
    compute_registry_hash,
    validate_registry,
    write_export,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        type=Path,
        default=EXPORT_PATH,
        help="Export path (default: artifacts/taxonomy/CANONICAL_TRACK_REGISTRY.export.json)",
    )
    parser.add_argument(
        "--commit-sha",
        default=None,
        help="Override source_commit_sha (default: git rev-parse HEAD)",
    )
    args = parser.parse_args()

    errors = validate_registry()
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    export = write_export(path=args.out, source_commit_sha=args.commit_sha)
    print(f"Wrote {args.out}")
    print(f"registry_hash={export['registry_hash']}")
    print(f"source_commit_sha={export['source_commit_sha']}")
    print(f"track_count={export['track_count']}")
    # Stability check: recompute hash independently
    assert export["registry_hash"] == compute_registry_hash()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
