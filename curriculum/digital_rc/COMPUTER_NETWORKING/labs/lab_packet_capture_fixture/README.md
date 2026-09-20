# lab_packet_capture_fixture — Authorized fixture frame parse (not cafe Wireshark)

Parse classroom-crafted frames only. authorized_fixture must be true. No live capture on networks you do not own.

## Student artifact
Keys: `frames, ethertype, dst_ip, authorized_fixture`.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_packet_capture_fixture --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_packet_capture_fixture --empty
```

