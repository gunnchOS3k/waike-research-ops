# Week 10: Backbone design packet — documentation numbers, recomputed

NIF-5A10 closes the term with a design packet for the regional backbone that the class has been building. It uses only documentation numbers: an autonomous system number from 64496 to 64511, here 64500, and an IPv6 prefix inside 2001:db8::/32, here 2001:db8:4400::/48. Using a real company's ASN or prefix in a training packet can leak into configurations and hijack someone else's traffic, so the reviewer rejects it on sight. The packet recomputes rather than restates: the 1,145 km route's propagation delay, the availability of the redundant core with its serial power feed and uplink compared with the 0.999 target, and the 6.4 dB optical margin. It cites RFC 4271, 5952, 7323, and 1034 for the behaviour it relies on. The final line says plainly that the packet is a classroom exercise and makes no claim about production peering or real customer service. Mentors pick one number at random and ask the author to derive it at the whiteboard.

## Worked example

ASN 64500, prefix 2001:db8:4400::/48, 1,145 km → 5.6067 ms, availability 0.9993991 vs target 0.999 met, margin 6.4 dB, production_peering_claim false
