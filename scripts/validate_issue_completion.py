#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.issue_completion import ISSUE_EVIDENCE, evidence_ok

def main() -> int:
    missing = []
    for num, paths in sorted(ISSUE_EVIDENCE.items()):
        if not evidence_ok(num):
            missing.append(num)
    if missing:
        print("FAIL issues", missing)
        return 1
    print("PASS validate-issue-completion", len(ISSUE_EVIDENCE), "issues")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
