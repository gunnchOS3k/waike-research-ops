# lab_vlan_mac — VLAN-aware MAC table

aa:aa:aa:aa:aa:10 in VLAN 20 exits Gi1/0/8. The same MAC in VLAN 30 is a miss.

## Student artifact
Keys: `out_port, vlan30_leak`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_vlan_mac --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_vlan_mac --empty
```

Leaking the VLAN 20 port into VLAN 30 fails isolation.
