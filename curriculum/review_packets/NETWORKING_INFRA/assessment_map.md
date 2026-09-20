# Assessment map — NETWORKING_INFRA

## Philosophy

WAIKE assessments prefer **artifacts + runnable checks** over exam-heavy gates.  
Quizzes (if present) are practice/formative unless explicitly labeled summative.

## Assessment artifacts on disk

- `curriculum/digital_rc/NETWORKING_INFRA/assessments/final_knowledge.json`
- `curriculum/digital_rc/NETWORKING_INFRA/assessments/final_practical.json`
- `curriculum/digital_rc/NETWORKING_INFRA/assessments/mid_course.json`

## Assignments → deliverables

| Assignment | Deliverable | Gap |
|------------|-------------|-----|
| `a01.md` | the sticky-note stack for a TLS web fetch from Pier to a library cache. Label who reads each header. No vendor GUI screenshots required | ok |
| `a02.md` | lab_cidr_math | ok |
| `a03.md` | a 6-row MAC/VLAN table for Pier/Yard/Shed. Include one intentional miss and explain why flooding stays in-VLAN | ok |
| `a04.md` | lab_datapath | ok |
| `a05.md` | an AIMD table for 8 RTTs starting cwnd=8 MSS with a loss at RTT 3. State rwnd vs cwnd in one sentence each | ok |
| `a06.md` | a one-page loop postmortem for the Packet Range with a blocking-port diagram. Include BPDU guard in the 'what we change' section | ok |
| `a07.md` | lab_spf_routing | ok |
| `a08.md` | lab_dns_resolution | ok |
| `a09.md` | a 6-line ACL for the Packet Range edge. Include one rogue-DHCP mitigation in prose (not a stolen Cisco snippet) | ok |
| `a10.md` | intent JSON, datapath result, packet trace, and the guest-VLAN redesign. Pair | ok |

## Rubrics → criteria

| Rubric | Criteria count | Sample | Gap |
|--------|----------------|--------|-----|
| `COMPUTER_NETWORKING-assignment.md` | 3 | sliced_frame, spf_recompute, no_vendor_gui | ok |
| `COMPUTER_NETWORKING-final-knowledge.md` | 2 | original_stems, stp_spf_acl | ok |
| `COMPUTER_NETWORKING-lab.md` | 4 | datapath_parse, ttl1_drop, lpm, acl_order | ok |
| `COMPUTER_NETWORKING-mid.md` | 2 | original_stems, encap_cidr_tcp | ok |
| `COMPUTER_NETWORKING-portfolio.md` | 3 | trace, intent, no_ccna_claim | ok |
| `COMPUTER_NETWORKING-practical.md` | 3 | student_parse, ttl_header, negatives | ok |
| `COMPUTER_NETWORKING-project.md` | 3 | intent_json, guest_isolated, eight_minutes | ok |
| `COMPUTER_NETWORKING-quiz.md` | 2 | range_numbers, key_hidden | ok |

## Capstone / portfolio

- Portfolio path: `curriculum/digital_rc/NETWORKING_INFRA/portfolio/`
- Group/project paths under package `projects/` if present.

## Claim boundary

This map inventories files; it does **not** assert psychometric validity or that a live cohort was graded.
