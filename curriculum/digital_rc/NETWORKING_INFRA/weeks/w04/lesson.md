# Week 4: BGP best path — policy first, then the shorter story

NIF-5404 asks why traffic to a partner network leaves through the long transit path instead of the direct one. Border Gateway Protocol routers hear several routes to the same prefix and pick one by walking an ordered list of attributes, stopping at the first that differs. This course uses a simplified order: highest local preference, shortest AS_PATH, lowest origin code with IGP before EGP before incomplete, lowest MED, then lowest router ID. Local preference is the operator's own policy, so it outranks everything about the route's length. Here R1 offers a one-hop path through documentation AS 64500 but carries local preference 100, while R2 and R3 both carry 200, so R1 is out at the first step even though its path is shortest. R2 and R3 each have four AS numbers, a tie, so the origin decides: R2 is IGP and R3 is EGP, and R2 wins. The deciding attribute is origin. Real routers add steps such as weight and eBGP-over-iBGP; RFC 4271 is the reference, and vendor documents list their full order.

## Worked example

R1 lp100 [64500]; R2 lp200 len4 IGP; R3 lp200 len4 EGP → local_pref removes R1, AS_PATH ties, origin IGP<EGP → R2
