#!/usr/bin/env python3
"""Map open issues to required artifact paths from ISSUE_COMPLETION_MASTER_TABLE."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT / ".audit/ISSUE_COMPLETION_MASTER_TABLE.csv"
OUT = ROOT / ".audit/ARTIFACT_COMPLETION_MATRIX.md"


def main() -> int:
    lines = ["# Artifact completion matrix\n", "| Issue | Artifact | Evidence |\n", "|-------|----------|----------|\n"]
    with TABLE.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ev = (row.get("current_evidence") or "").replace(";", "<br>")
            lines.append(
                f"| #{row['issue_number']} {row['issue_title'][:40]} | `{row.get('artifact_required', '')}` | {ev} |\n"
            )
    OUT.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
