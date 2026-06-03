#!/usr/bin/env python3
"""Classify open issues and write ISSUE_COMPLETION_MASTER_TABLE.csv."""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from waike_curriculum.issue_completion import ISSUE_EVIDENCE, evidence_ok

AUDIT = ROOT / ".audit"
MAIN_ONLY = {9, 10, 11, 14}  # substantive docs existed pre-structure


def priority(title: str) -> str:
    if "P0" in title:
        return "p0"
    if "P1" in title:
        return "p1"
    if "P2" in title:
        return "p2"
    return "p?"


def classify(num: int) -> str:
    if num in MAIN_ONLY and (ROOT / ISSUE_EVIDENCE[num][0]).exists():
        return "ALREADY_DONE_ON_MAIN"
    if evidence_ok(num):
        return "DONE_ON_BRANCH_NEEDS_PR_MERGE"
    return "NEEDS_WORK_THIS_PASS"


def main() -> int:
    issues_path = AUDIT / "open_issues.json"
    if not issues_path.exists():
        import subprocess
        subprocess.run([sys.executable, str(ROOT / "scripts/audit_open_issues.py")], check=True)
    issues = json.loads(issues_path.read_text())
    rows = []
    for i in issues:
        num = i["number"]
        cls = classify(num)
        ev = "; ".join(ISSUE_EVIDENCE.get(num, []))
        rows.append({
            "issue_number": num,
            "issue_title": i["title"],
            "url": i["url"],
            "priority": priority(i["title"]),
            "classification": cls,
            "artifact_required": ISSUE_EVIDENCE.get(num, ["TBD"])[0],
            "current_evidence": ev,
            "missing_work": "" if evidence_ok(num) else "implement",
            "action_taken": "implement_issue_completion.py",
            "files_changed": ev,
            "validation_command": "make validate-issue-completion",
            "closure_decision": "close_now" if cls == "ALREADY_DONE_ON_MAIN" else "fixes_in_pr",
            "close_now": cls == "ALREADY_DONE_ON_MAIN",
            "fixes_in_pr": cls == "DONE_ON_BRANCH_NEEDS_PR_MERGE",
            "stay_open_reason": "" if evidence_ok(num) else "missing artifacts",
        })
    path = AUDIT / "ISSUE_COMPLETION_MASTER_TABLE.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    report = AUDIT / "ISSUE_COMPLETION_MASTER_REPORT.md"
    report.write_text(
        f"# Issue completion report\n\nFetched: {len(issues)} open issues.\n\n"
        + "\n".join(f"- #{r['issue_number']}: {r['classification']}" for r in rows),
        encoding="utf-8",
    )
    print(f"Classified {len(rows)} issues")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
