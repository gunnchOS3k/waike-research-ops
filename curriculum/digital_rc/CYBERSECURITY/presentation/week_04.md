# Week 4 presentation — SIEM triage — bursts are a look, not a conviction

## Slide 1 — Cold open
counts ada=4, cal=1, threshold=3 → bursts=['ada']. Note: burst, not attacker.

## Slide 2 — Teaching beat
AUTH_FAIL lines for ada four times from 10.20.30.5 cross the threshold of 3. cal fails once. bea succeeds. Your note says 'burst on ada,' not 'ada is the attacker.' Bursts are a look. Conviction needs more.

## Slide 3 — Live work
Write the Harbor note on the board: 'burst on ada' vs 'ada is the attacker'. Only the first passes.

## Speaker notes
Week 8 is a toy parser. Anyone opening nmap on the campus /24 fails the course ethic, not just the lab.
