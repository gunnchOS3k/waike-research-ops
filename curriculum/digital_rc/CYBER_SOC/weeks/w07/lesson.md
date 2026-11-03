# Week 7: CVSS v3.1 by hand — from vector string to severity band

SOC-2707 is the second NO_AI week, because a desk that only reads scores off a website cannot defend them in a patch meeting. The FIRST CVSS v3.1 base score turns eight metrics into a number. Impact starts from the confidentiality, integrity, and availability weights, 0.56 for High, 0.22 for Low, 0 for None, combined as ISS = 1 − (1 − C)(1 − I)(1 − A). For an unchanged scope, impact is 6.42 × ISS. Exploitability is 8.22 × attack vector × attack complexity × privileges required × user interaction, where a network vector weighs 0.85 and low complexity 0.77. For the familiar AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H vector, ISS is about 0.9148, impact about 5.873, exploitability about 3.887, and their sum rounds up to 9.8, Critical. Roundup means the next tenth upward, not the nearest, which is where hand scorers slip. A local, low-privilege flaw that only leaks data, AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N, lands at 5.5, Medium. The base score describes the flaw, not your network; asset value enters next week.

## Worked example

AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H → ISS 0.9148, impact 5.873, exploitability 3.887 → Roundup 9.8 Critical; AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N → 5.5 Medium
