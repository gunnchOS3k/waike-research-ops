# Week 10: Shift handoff — open incidents, NIST phases, and clean boundaries

SOC-2A10 closes the night. A handoff is the document the day shift reads with its first coffee, so it must be complete without you in the room. List every open incident with its ATT&CK technique ID, the NIST SP 800-61 phase it is in, and a named next owner. The phases are preparation, detection and analysis, containment with eradication and recovery, and post-incident activity; saying 'containment' tells the reader which actions are already done and which are waiting. Carry the shift's MTTD and MTTR from last week's calculation rather than rounding them in your head, and say what changed in the rules you tuned. Two boundaries close every Night Shift Desk packet. It contains no real customer data, only the course's synthetic logs and documentation addresses, and it contains no offensive tooling: the desk detects, contains, and documents; it does not build exploits or scan systems it does not own. Mentors check the packet against six or more passed labs and ask you to walk one incident from first log line to current phase out loud.

## Worked example

I4 open: T1486, containment_eradication_recovery, next owner day-shift lead; MTTD 33, MTTR 82; real_customer_data false; offensive_tooling false
