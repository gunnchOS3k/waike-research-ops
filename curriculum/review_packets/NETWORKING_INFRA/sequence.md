# Sequence — NETWORKING_INFRA

Complete module/week sequence from `NETWORKING_INFRA` `course.json`.

| Week | Title | Lesson ID | Lab ID |
|------|-------|-----------|--------|
| 1 | Packets are chopped on purpose | `NETWORKING_INFRA-w01` | `lab_cidr_math` |
| 2 | CIDR as a land survey, not a guessing game | `NETWORKING_INFRA-w02` | `lab_cidr_math` |
| 3 | The MAC closet — learning, flooding, and VLAN 20 | `NETWORKING_INFRA-w03` | `lab_vlan_mac` |
| 4 | Forwarding plane — TTL, LPM, and a crafted IPv4 frame | `NETWORKING_INFRA-w04` | `lab_datapath` |
| 5 | Reliability on an unreliable wire — sequences, ACKs, AIMD on paper | `NETWORKING_INFRA-w05` | `lab_transport_ports` |
| 6 | When VLANs meet a loop — STP as a circuit breaker | `NETWORKING_INFRA-w06` | `lab_wifi_fundamentals` |
| 7 | Four-router town — SPF beats the scenic route | `NETWORKING_INFRA-w07` | `lab_spf_routing` |
| 8 | DHCP, DNS, NAT — services that lie for us on purpose | `NETWORKING_INFRA-w08` | `lab_dns_resolution` |
| 9 | ACLs that actually order, and the telnet we refuse | `NETWORKING_INFRA-w09` | `lab_packet_capture_fixture` |
| 10 | Campus edge capstone — intent files and a datapath proof | `NETWORKING_INFRA-w10` | `lab_ops_runbook` |

## Syllabus excerpt (source)

```
# Networking Infrastructure — Packet Range Campus Edge
## Who this is for
Operators who need campus edge literacy: models, L2/L3, DNS/DHCP, Wi-Fi fundamentals, troubleshooting, and security basics without unauthorized capture.
## Tracks and academy
- course_id / track_id: NETWORKING_INFRA
- Legacy shared content package: COMPUTER_NETWORKING/
- Academy: ACADEMY_NETWORKING
## Duration
Ten weeks (~8–10 hours/week). Shared labs live under `COMPUTER_NETWORKING/labs/`; this entry re-exports them under canonical track_id `NETWORKING_INFRA`.
## Weekly map
- Week 01: Network models & encapsulation on the Packet Range
- Week 02: IP addressing & subnetting as land survey
- Week 03: Ethernet / L2 switching & VLANs
- Week 04: Forwarding plane — TTL, LPM, crafted frames
- Week 05: Transport — TCP reliability & ports
- Week 06: Wi-Fi fundamentals for campus edge
- Week 07: Routing — SPF on the four-router town
- Week 08: DNS / DHCP / NAT service honesty
- Week 09: Security basics & authorized fixture capture
- Week 10: Modern ops runbook & campus edge capstone
## Assessments
Weekly quizzes, mid (20), final (24), practical labs (10), portfolio. Answer keys stay in `instructor/answer_keys.json` and are **not** in learner ingest.
## Claim boundary
Aligns to public standards topic labels only. Does not grant vendor certs. Shared lesson/lab bodies referenced via content_ref — not blind full-tree duplication.
```

## Duration note

Package default is **10 weeks**. Program files may also list workshop/bootcamp/apprenticeship formats — those are alternate delivery envelopes, not alternate content claims.
