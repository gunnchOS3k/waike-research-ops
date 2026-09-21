# lab_packet_capture_fixture — Authorized packet-capture fixture summary

Summarize fixture frames only. authorized_fixture must be true. No offensive payload crafting.

## Student artifact
Keys: `frames, ethertype, dst_ip, authorized_fixture`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_packet_capture_fixture --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_packet_capture_fixture --empty
```

authorized_fixture=false fails.
