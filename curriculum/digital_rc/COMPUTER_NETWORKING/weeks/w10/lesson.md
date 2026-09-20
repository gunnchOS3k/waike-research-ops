# Week 10: Campus edge capstone — intent files and a datapath proof

You will ship a JSON intent file: VLANs, prefixes, ACL order, NAT, and the four-router costs. A tiny validator will reject missing next-hops. That is the automation domain without pretending we built a controller fabric.

The practical exam is the datapath lab plus a written trace of one packet from Pier to Roof including VLAN, LPM, TTL, and ACL. If those four nouns are not in the trace, the practical is incomplete.

Group project: redesign the Packet Range for a public Saturday with a guest VLAN that cannot reach Roof management. Present for eight minutes. No slide template from the old campus UPNOW generator — your topology is specific.

Career: this course aligns to CCNA v1.1 domains and to CS144's build-the-path ethos. It does not grant CCNA. It does not include Stanford solutions. If a recruiter asks 'did you pass CCNA,' the honest answer is 'I can show a datapath trace and an intent file,' not 'yes.' That sentence belongs in the portfolio.

## Worked example

Intent JSON must include prefix 10.20.40.0/24 nh via Yard, ACL deny 23, datapath ok=true.
