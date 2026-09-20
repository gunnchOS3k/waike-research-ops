# lab_transport_ports — Transport ports and three-way handshake

Map https/dns/ssh ports; handshake SYN→SYN-ACK→ACK; refuse_telnet true.

## Student artifact
Keys: `map, handshake, refuse_telnet`.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_transport_ports --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_transport_ports --empty
```

