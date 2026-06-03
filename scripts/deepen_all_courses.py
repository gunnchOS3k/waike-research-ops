#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from waike_curriculum.depth_generators import deepen_all, portfolio_evidence_index

if __name__ == "__main__":
    deepen_all()
    portfolio_evidence_index()
    print("Deepened all courses")
