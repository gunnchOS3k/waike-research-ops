# PR and issue-close handoff (run in Terminal with `gh auth login`)

## Branch pushed

- **Branch:** `issue-completion-student-instructor-readiness-audit`
- **Commit:** `9dd986c` (see `git rev-parse HEAD`)
- **Compare:** https://github.com/gunnchOS3k/waike-research-ops/compare/main...issue-completion-student-instructor-readiness-audit

## Create PR

```bash
cd repos/waike-research-ops
bash scripts/create_or_update_issue_completion_pr.sh
```

Or:

```bash
gh pr create --repo gunnchOS3k/waike-research-ops --base main \
  --head issue-completion-student-instructor-readiness-audit \
  --title "Complete WAIKE issues and add student/instructor readiness audit" \
  --body-file .audit/PR_BODY.md
```

(Copy PR body from `FINAL_WAIKE_ISSUE_COMPLETION_AND_READINESS_AUDIT.md` or script output.)

## Close issues already on main

```bash
bash scripts/close_completed_issues.sh
```

Targets: #9, #10, #11, #14

## Comment on branch-fixed issues (optional)

```bash
REPO=gunnchOS3k/waike-research-ops
for n in 1 2 3 4 5 6 7 12 13 15 16 17 18 19 20 21 22 23 24 25 26 27 28; do
  gh issue comment "$n" --repo "$REPO" --body "Implemented on branch issue-completion-student-instructor-readiness-audit. Evidence in repo paths from .audit/ISSUE_COMPLETION_MASTER_TABLE.csv. Validation: make e2e. Closes when PR merges (Fixes #$n)."
done
```

**Do not merge** until Edmund approves. **Do not enable auto-merge.**
