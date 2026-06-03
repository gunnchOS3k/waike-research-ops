#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_curriculum.generators import generate_all, generate_results_syllabus, seed_course
from waike_curriculum.catalog import load_catalog


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--all", action="store_true")
    p.add_argument("--course")
    args = p.parse_args()
    if args.all:
        generate_all()
        print("Generated all syllabi and base curriculum")
        return 0
    if args.course:
        for c in load_catalog().get("courses", []):
            if c["course_id"] == args.course:
                seed_course(c)
                generate_results_syllabus(c)
                print(f"Generated {args.course}")
                return 0
        print("Unknown course", args.course)
        return 1
    generate_all()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
