#!/bin/bash
set -e
REPO=gunnchOS3k/waike-research-ops
BRANCH=issue-completion-student-instructor-readiness-audit
git push -u origin "$BRANCH" || true
FIXES=$(python3 -c "
import csv
from pathlib import Path
for r in csv.DictReader(open('.audit/ISSUE_COMPLETION_MASTER_TABLE.csv')):
    if r.get('fixes_in_pr') == 'True':
        print(f\"Fixes #{r['issue_number']}\")
")
gh pr create --repo "$REPO" --base main --head "$BRANCH" \
  --title "Complete WAIKE issues and add student/instructor readiness audit" \
  --body "$(cat <<EOF
## Summary
Completes open WAIKE issue artifacts (templates, standards, capstones, training, portfolio, localization, evaluation) and adds student/instructor/placeholder audits.

## Issues fixed by this PR
$FIXES

## Validation
- make e2e
- make validate-issue-completion

Do not merge until Edmund reviews.
EOF
)" 2>/dev/null || echo "Compare: https://github.com/$REPO/compare/main...$BRANCH"
