# Week 10: DevSecOps + incident — automate recoveries without heroics

Capstone: an incident playbook that rolls back, rotates a leaked stub token, and records timeline timestamps. Ticket FC-4A03 fails if heroics=true (solo undocumented fix) or if automation_runbook_id is missing. Infra automation means the runbook id is executable in the lab sense — not a vibe doc.

heroics=false; automation_runbook_id='RB-FC-rollback'; token_rotated=true; timeline has detect/contain/recover.

Incident runbook RB-FC-rollback: heroics=false, token_rotated=true, timeline with detect/contain/recover stamps. Solo undocumented fixes fail honesty.

DevSecOps trio: rollback, rotate, runbook. Missing automation_runbook_id fails the capstone lab. Ship perms/CI/SLO/rollback/probes/incident JSON without cert claims.

Heroics look fast and teach nothing. ForgeCloud prefers a boring executable runbook id another on-call can run at 02:00 without calling you.

## Worked example

RB-FC-rollback; heroics=false; token_rotated=true; three timeline stamps.
