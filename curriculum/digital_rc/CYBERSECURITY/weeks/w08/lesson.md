# Week 8: Detection, triage & safe vuln concepts

**Track:** CYBER_SOC
**content_ref:** `../CYBERSECURITY/weeks/w08/lesson.md`

## Objectives
- Detect length-lie in toy parser
- Safe parser raises
- No shellcode/live scan

## Body (track overlay)
Authorized toy parser. Defensive bounds checks only.

Shared lesson body is maintained under the legacy package at `../CYBERSECURITY/weeks/w08/lesson.md`. Read that module in full; this overlay adds track-id framing, assessment mode, and claim refusals.

## Worked example
unsafe(\x14short) returns a short slice (the lie). safe(\x14short) raises ValueError. safe(\x04abcd)==b'abcd'.

## Assessment mode
NO_AI

## Claim refusals
- No shellcode
- No malware
- No random IP scans
