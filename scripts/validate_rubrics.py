#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQ = [
    "rubrics/master_rubric.yaml",
    "rubrics/teamwork_rubric.yaml",
    "rubrics/documentation_rubric.yaml",
    "rubrics/presentation_rubric.yaml",
    "rubrics/technical_accuracy_rubric.yaml",
    "rubrics/ethics_privacy_rubric.yaml",
    "rubrics/reproducibility_rubric.yaml",
    "rubrics/portfolio_rubric.yaml",
]


def main() -> int:
    missing = [p for p in REQ if not (ROOT / p).exists()]
    if missing:
        print("FAIL", missing)
        return 1
    print("PASS validate-rubrics")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
