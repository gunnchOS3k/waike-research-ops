# lab_cidr_math — Pier /26 and /28

10.20.30.40/26 network is 10.20.30.0, not .40. Usable 62 and 14. This is bitwise work, not a GUI.

## Student artifact
Keys: `cases`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_cidr_math --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_cidr_math --empty
```

Using the host address as the network on /26 is the package negative.

## Prefix conventions and input verification

Submit a nonempty `cases` list, up to 64 cases. Each case needs a string IPv4 `cidr`, calculated `network` and `broadcast` strings, and an integer `usable` count. Boolean values are not counts. For ordinary /0–/30 subnet arithmetic, subtract network and broadcast addresses; for /31 use the point-to-point convention (two), and for /32 use the single host-route address (one). The `broadcast` output for /31 and /32 is the library's numerical upper-bound property, not a claim of an operational directed broadcast. RFC 4632 section 3.1: https://www.rfc-editor.org/rfc/rfc4632.html. No packets are sent.

Independent practice: calculate a /30, /31 and /32 using documentation addresses. Run the CLI with your artifact. Then deliberately submit zero usable addresses for /32 and verify that the check fails. Empty/malformed lists must fail rather than produce a passing result or an uncaught parser exception.
