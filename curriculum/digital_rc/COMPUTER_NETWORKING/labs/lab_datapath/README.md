# lab_datapath — Crafted Ethernet+IPv4 path

Parse dest MAC, ethertype, TTL at IP[8], proto, dest IP. LPM must pick the /24 (eth1). Craft a TTL=1 copy of the same header, decrement that byte, and refuse to forward when the result is 0. `(1-1)==0` without parsing is not accepted.

## Student artifact
Keys: `dst_mac, ethertype, ttl, proto, dst_ip, lpm_iface, ttl1_forwarded, ttl1_after_decrement`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_datapath --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_datapath --empty
```

ttl1_forwarded true, or after_decrement 1, fails the drop check.
