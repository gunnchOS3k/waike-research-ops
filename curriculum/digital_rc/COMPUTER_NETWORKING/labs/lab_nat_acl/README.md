# lab_nat_acl — Edge ACL and inside NAT

deny 23, permit 443, deny *. Inside is 10.20.30.14. Order matters.

## Student artifact
Keys: `telnet, https, discard, nat_inside`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_nat_acl --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_nat_acl --empty
```

permit telnet fails the edge story.
