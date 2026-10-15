# lab_dns_resolution — Stub then cache

First lookup walks auth (203.0.113.14). Second is cache.

## Student artifact
Keys: `first_how, second_how, ip`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_dns_resolution --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_dns_resolution --empty
```

Calling the first hit a cache miss-order fails.

## Source-bound practice and limits

The historical first_how/second_how artifact is a simplified declared-state contract, not proof of real recursive DNS traffic. The new PositiveDnsCache exercise executes positive A-record expiry against a local dictionary, including exact expiry and zero TTL. Its fixture_authority label describes that local lookup, not a root/TLD/authoritative exchange. Do not translate not_in_fixture into a measured NXDOMAIN claim. See learner_exercises/packet_model/README.md for exact execution, expected results, independent evidence criteria and troubleshooting. No production network configuration or physical validation is performed.
