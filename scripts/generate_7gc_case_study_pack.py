#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.catalog import FLAGSHIP_CASE_STUDIES
from waike_curriculum.generators import seed_case_studies, write


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--site")
    p.add_argument("--all", action="store_true")
    args = p.parse_args()
    seed_case_studies()
    sites = FLAGSHIP_CASE_STUDIES.keys() if args.all else [args.site] if args.site else list(FLAGSHIP_CASE_STUDIES.keys())
    for site in sites:
        if site not in FLAGSHIP_CASE_STUDIES:
            print("Unknown site", site)
            return 1
        cases = FLAGSHIP_CASE_STUDIES[site]
        body = f"# Case studies — {site}\n\n" + "\n".join(f"- {c['title']}" for c in cases)
        write(ROOT / "results" / "case_study_packs" / f"{site}_case_studies.md", body)
    print("Generated case study packs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
