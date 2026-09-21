# Assessment map — CYBER_SOC

## Philosophy

WAIKE assessments prefer **artifacts + runnable checks** over exam-heavy gates.  
Quizzes (if present) are practice/formative unless explicitly labeled summative.

## Assessment artifacts on disk

- `curriculum/digital_rc/CYBER_SOC/assessments/final_knowledge.json`
- `curriculum/digital_rc/CYBER_SOC/assessments/final_practical.json`
- `curriculum/digital_rc/CYBER_SOC/assessments/mid_course.json`

## Assignments → deliverables

| Assignment | Deliverable | Gap |
|------------|-------------|-----|
| `a01.md` | a one-page Harbor governance memo: CIA applied to the ticket-summarizer bot, one GRC owner, and one prohibited data class | ok |
| `a02.md` | the identity lifecycle for harbor-bot: request, approve, issue, rotate, revoke. Name the human owner | ok |
| `a03.md` | three sentences on shared responsibility if tickets moved to a SaaS. No vendor brochure language | ok |
| `a04.md` | a three-sentence incident-look note from the fixture. Name burst users. No secrets | ok |
| `a05.md` | lab_hardening_baseline | ok |
| `a06.md` | a stolen-laptop tabletop with timestamps, identity actions, and a 'do not' list that includes punching holes in the SOC zone | ok |
| `a07.md` | lab_incident_playbook | ok |
| `a08.md` | a 5-line responsible-disclosure note template with no exploit code | ok |
| `a09.md` | lab_forensics_timeline | ok |
| `a10.md` | design (≤2 pages), policy checker output, lab JSON, and the scope paragraph. Pair | ok |

## Rubrics → criteria

| Rubric | Criteria count | Sample | Gap |
|--------|----------------|--------|-----|
| `CYBERSECURITY-assignment.md` | 3 | named_identities, no_secrets, authorized_only | ok |
| `CYBERSECURITY-final-knowledge.md` | 2 | original_stems, harden_ir_parser | ok |
| `CYBERSECURITY-lab.md` | 4 | burst_note, bot_rbac, toy_parser, ir_order | ok |
| `CYBERSECURITY-mid.md` | 2 | original_stems, cc_2026_domains | ok |
| `CYBERSECURITY-portfolio.md` | 3 | seven_json, cannot_claim, no_cert_claim | ok |
| `CYBERSECURITY-practical.md` | 3 | empty_fails, no_network, bot_negative | ok |
| `CYBERSECURITY-project.md` | 3 | design_first, pii_reject, bot_not_closer | ok |
| `CYBERSECURITY-quiz.md` | 2 | harbor_words, key_hidden | ok |

## Capstone / portfolio

- Portfolio path: `curriculum/digital_rc/CYBER_SOC/portfolio/`
- Group/project paths under package `projects/` if present.

## Claim boundary

This map inventories files; it does **not** assert psychometric validity or that a live cohort was graded.
