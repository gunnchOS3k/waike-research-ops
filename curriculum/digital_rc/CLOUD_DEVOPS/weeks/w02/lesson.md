# Week 2: Git on ForgeCloud — history you can roll back

Ticket FC-4206 needs a release branch that is 2 commits ahead of main with a known conflict path services/api/health.py. You will report ahead/behind and list conflict files. Force-push to main is forbidden in the course ethic — same as production.

ahead=2 behind=0 conflict_files=['services/api/health.py']; force_push_main=false.

Release branch state: ahead=2, behind=0, conflict on services/api/health.py. force_push_main must stay false — recoverable history beats a rewritten main.

Write a merge plan that integrates without destroying reviewers’ commits. Behind>0 means integrate main first; do not cosplay by force-pushing past the conflict.

Git is the rollback substrate for later weeks. If history is a vibe, digest pins and incident timelines have nothing solid to cite.

Week 2 close for CLOUD_DEVOPS: ticket work ends when the lab JSON fields for `lab_git_state` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

ahead 2 / behind 0; conflict on services/api/health.py; no force-push main.
