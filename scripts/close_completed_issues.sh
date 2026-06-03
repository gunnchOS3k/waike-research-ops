#!/bin/bash
# Close ONLY issues classified ALREADY_DONE_ON_MAIN. Run: gh auth login first.
set -e
REPO=gunnchOS3k/waike-research-ops
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$ROOT/.audit/ISSUE_CLOSE_LOG.md"
echo "# Issue close log" > "$LOG"
python3 "$ROOT/scripts/classify_issue_completion.py"
while IFS=, read -r num title _ _ _ _ _ _ _ _ _ _ close _; do
  [[ "$num" == "issue_number" ]] && continue
  [[ "$close" != "True" ]] && continue
  echo "Closing #$num" | tee -a "$LOG"
  gh issue close "$num" --repo "$REPO" --reason completed --comment "Completed on main. Evidence in repo docs. Validation: make validate-issue-completion. Closed by issue-completion audit." 2>>"$LOG" || echo "gh failed for #$num" >>"$LOG"
done < <(tail -n +2 "$ROOT/.audit/ISSUE_COMPLETION_MASTER_TABLE.csv")
