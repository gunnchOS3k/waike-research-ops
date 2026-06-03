#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.issue_completion import implement_all

if __name__ == "__main__":
    implement_all()
    print("Implemented issue completion artifacts")
