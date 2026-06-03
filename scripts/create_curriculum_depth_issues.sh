#!/bin/bash
# Run after: gh auth login
set -e
REPO=gunnchOS3k/waike-research-ops
for f in issue_bodies/curriculum_depth/*.md; do
  title=$(head -1 "$f" | sed 's/^# //')
  gh issue create --repo "$REPO" --title "$title" --body-file "$f" --label curriculum,7gc,priority:p1 || true
done
