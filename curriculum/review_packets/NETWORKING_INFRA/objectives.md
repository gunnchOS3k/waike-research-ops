# Objectives — NETWORKING_INFRA

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: Packets are chopped on purpose
  - Complete the week contract: Packets are chopped on purpose.
  - Reproduce worked example: A 2000-byte application buffer on a 1500 MTU path becomes at least two IP datagrams. Peel Ethernet first (ethertype 0x0800), then IP, then TCP.
  - The WAIKE Packet Range is a table, a switch, and four Raspberry-class endpoints named Pier, Yard, Shed, and Roof.
### Week 2: CIDR as a land survey, not a guessing game
  - Complete the week contract: CIDR as a land survey, not a guessing game.
  - Reproduce worked example: 10.20.30.40/26 → net 10.20.30.0 bcast 10.20.30.63 usable 62. 10.20.30.80/28 → net 10.20.30.80 bcast 10.20.30.95 usable 14.
  - 10.20.30.40/26 is not 'a class C with a funny number.' /26 means 26 bits of network, 6 bits of host, 64 addresses, network 10.20.30.0, broadcast 10.20.30.63, 62 usable if you still believe in network and broadcast addres
### Week 3: The MAC closet — learning, flooding, and VLAN 20
  - Complete the week contract: The MAC closet — learning, flooding, and VLAN 20.
  - Reproduce worked example: mac_table[(aa:aa:aa:aa:aa:10, 20)] = Gi1/0/8. Lookup with VLAN 30 misses. Isolation holds.
  - Pier hangs off Gi1/0/8 on VLAN 20.
### Week 4: Forwarding plane — TTL, LPM, and a crafted IPv4 frame
  - Complete the week contract: Forwarding plane — TTL, LPM, and a crafted IPv4 frame.
  - Reproduce worked example: dst 10.20.40.9 matches /24 better than /16. nh 10.20.30.1 iface eth1. TTL 4→3. Host route /32 wins when present.
  - This is the deep data-path week.
### Week 5: Reliability on an unreliable wire — sequences, ACKs, AIMD on paper
  - Complete the week contract: Reliability on an unreliable wire — sequences, ACKs, AIMD on paper.
  - Reproduce worked example: seq=1000 len=200 → ACK 1200 on full receipt. cwnd 10, loss → 5, then 6,7,8... on additive increase per RTT without further loss.
  - TCP (current spec RFC 9293) pretends the wire is reliable by numbering bytes and refusing to live on hope.
### Week 6: When VLANs meet a loop — STP as a circuit breaker
  - Complete the week contract: When VLANs meet a loop — STP as a circuit breaker.
  - Reproduce worked example: Two access cables into one closet without STP → storm. BPDU guard on access would err-disable the volunteer mini-switch instead of electing it root.
  - Rapid PVST+ is a CCNA v1.1 phrase.
### Week 7: Four-router town — SPF beats the scenic route
  - Complete the week contract: Four-router town — SPF beats the scenic route.
  - Reproduce worked example: dijkstra(A)['D']=4 via B. Scenic A-C-D=10 loses. Install 10.20.40.0/24 nh=Yard.
  - Routers A (Pier), B (Yard), C (Shed), D (Roof).
### Week 8: DHCP, DNS, NAT — services that lie for us on purpose
  - Complete the week contract: DHCP, DNS, NAT — services that lie for us on purpose.
  - Reproduce worked example: First resolve desk.gary.waike.example → 203.0.113.14 via auth_walk. Second → cache. NAT inside 10.20.30.14 outside 192.0.2.88.
  - DHCP hands out leases so Pier does not keep a paper IP ledger.
### Week 9: ACLs that actually order, and the telnet we refuse
  - Complete the week contract: ACLs that actually order, and the telnet we refuse.
  - Reproduce worked example: decide(23)=deny, decide(443)=permit, decide(9)=deny. NAT still maps the inside host.
  - An ACL is a story told top to bottom.
### Week 10: Campus edge capstone — intent files and a datapath proof
  - Complete the week contract: Campus edge capstone — intent files and a datapath proof.
  - Reproduce worked example: Intent JSON must include prefix 10.20.40.0/24 nh via Yard, ACL deny 23, datapath ok=true.
  - You will ship a JSON intent file: VLANs, prefixes, ACL order, NAT, and the four-router costs.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
