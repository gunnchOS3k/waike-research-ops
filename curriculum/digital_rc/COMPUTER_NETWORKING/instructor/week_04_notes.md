# Packet Range — instructor week 4

**Hex/graph on the board:** dst 10.20.40.9 matches /24 better than /16. nh 10.20.30.1 iface eth1. TTL 4→3. Host route /32 wins when present.

**Lab `lab_datapath`:** student must submit parse/table JSON. Empty fails.

**Pitfall:** Do not accept (1-1)==0 as a TTL story. Parse the TTL=1 frame.

No CS144 code, no CCNA dumps. Alignment JSON only.
