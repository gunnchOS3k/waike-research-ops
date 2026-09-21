# lab_transport_ports — Transport ports and handshake vocabulary

Map https/dns/ssh ports and list SYN/SYN-ACK/ACK. Refuse telnet as default admin path.

## Student artifact
Keys: `map, handshake, refuse_telnet`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_transport_ports --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_transport_ports --empty
```

Mapping https to 80 or allowing telnet fails.
