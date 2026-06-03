#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import load_catalog
from waike_curriculum.generators import generate_results_packets, seed_course


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--course")
    p.add_argument("--site")
    p.add_argument("--all", action="store_true")
    args = p.parse_args()
    for c in load_catalog().get("courses", []):
        if args.all or c["course_id"] == args.course:
            seed_course(c)
            generate_results_packets(c)
    print("Generated group project packs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
