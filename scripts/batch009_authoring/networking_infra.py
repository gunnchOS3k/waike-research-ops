"""NETWORKING_INFRA — Backbone Room. Authored week by week; numbers match batch009/labs_nif.py."""

COURSE_ID = "NETWORKING_INFRA"
PREFIX = "nif"
TITLE = "Networking and Internet Infrastructure — Backbone Room"
ACADEMY = "ACADEMY_NETWORKING"
KINESTHETIC = (
    "Ten Backbone Room change requests: budget fiber latency → write IPv6 canonically → size TCP windows → pick a BGP "
    "path → plan a DNS cutover → size CDN offload → budget an optical span → compute availability → read a 95th-percentile "
    "bill → submit a design packet."
)
SYLLABUS_HOOK = (
    "NETWORKING_INFRA COURSE_DIGITAL_RC: internet-scale infrastructure arithmetic — fiber propagation, IPv6 text and "
    "prefix math, bandwidth-delay product, BGP path selection, DNS caching, CDN offload, optical link budgets, "
    "availability in series and parallel, and 95th-percentile transit billing. Documentation ASNs and prefixes only. "
    "Distinct from COMPUTER_NETWORKING (campus LAN, subnetting, switching). Not student/teacher E6."
)
CAREER = {
    "roles": ["network_operations_center_trainee", "noc_technician_apprentice", "isp_field_support_assistant"],
    "nice_categories": ["operate_and_maintain", "oversee_and_govern"],
    "certs_aligned_not_granted": [
        "Cisco CCNA 200-301 network-fundamentals labels (PUBLIC_REFERENCE_ONLY; no exam items)",
        "IETF RFC 4271 / 5952 / 7323 / 1034 vocabulary (PUBLIC_REFERENCE_ONLY)",
    ],
}
NO_AI_WEEKS = [7, 9]

WEEKS = [
    {
        "title": "Fiber latency budget — light is slower in glass",
        "lab_id": "lab_nif_latency_budget",
        "worked_example": "1,145 km × 1.468 / 299,792.458 km/s = 5.6067 ms propagation; 1,500 B × 8 / 1 Gbit/s = 0.012 ms; one-way 5.6187 ms",
        "lesson": (
            "Change request NIF-5101 asks whether a new 1,145 km fiber route between two regional exchanges can promise "
            "game servers a one-way delay under six milliseconds. Light in a vacuum covers about 299,792 km each second, "
            "but glass slows it by the fiber's group index, about 1.468, so the signal moves at roughly 204,000 km/s. "
            "Divide the route length by that speed: 1,145 km takes about 5.6067 milliseconds. That is propagation, and no "
            "upgrade fixes it short of a straighter path. Serialization is the time to clock a packet's bits onto the wire: "
            "1,500 bytes is 12,000 bits, which takes 0.012 ms at one gigabit per second and would take ten times longer on "
            "a 100-megabit link. Add them for a one-way floor of about 5.619 ms, before any queueing or equipment delay. "
            "Route length is not the straight-line distance on a map; cables follow railways and roads, so ask for the "
            "measured route. Using the vacuum speed understates delay by about a third and leads to promises the backbone cannot keep."
        ),
        "assignment": "Submit lab_nif_latency_budget JSON for NIF-5101: route_km, packet_bytes, link_gbps, propagation_ms, serialization_ms, one_way_ms.",
        "quiz": [
            ("About how fast does light travel in fiber with index 1.468?", ["About 204,000 km/s", "About 300,000 km/s", "About 1,468 km/s", "About 100,000 km/s"], "c / n"),
            ("What is the propagation delay over 1,145 km of fiber?", ["About 5.61 ms", "About 3.82 ms", "About 11.45 ms", "About 0.56 ms"], "km × n / c"),
            ("How long does a 1,500-byte packet take to serialize at 1 Gbit/s?", ["0.012 ms", "1.5 ms", "0.0015 ms", "12 ms"], "12,000 bits"),
            ("Which delay can a faster link reduce?", ["Serialization", "Propagation", "Both equally", "Neither"], "bits per second"),
            ("Why ask for the measured route length?", ["Cables follow roads and railways, not straight lines", "Maps are illegal", "Fiber shrinks", "To add serialization"], "real path"),
            ("What error does using the vacuum speed of light cause?", ["Understates delay by about a third", "Overstates delay", "No error", "Doubles serialization"], "index"),
        ],
    },
    {
        "title": "IPv6 text and prefixes — one canonical way to write an address",
        "lab_id": "lab_nif_ipv6_text",
        "worked_example": "2001:0DB8:0000:0000:0001:0000:0000:0001 → 2001:db8::1:0:0:1; /48 site → /64 subnets: 2^16 = 65,536",
        "lesson": (
            "NIF-5202 began as an outage: two engineers searched the change log for the same router address and missed each "
            "other because they had typed it differently. IPv6 addresses are 128 bits, written as eight groups of four hex "
            "digits, and RFC 5952 sets one canonical text form so tools and people agree. Write hex in lowercase, drop "
            "leading zeros in each group, and replace the longest run of two or more all-zero groups with a double colon, "
            "choosing the first run if two are equally long. A single zero group stays as 0. So "
            "2001:0DB8:0000:0000:0001:0000:0000:0001 has two runs of two zero groups; the first one collapses and the result is "
            "2001:db8::1:0:0:1. The 2001:db8::/32 block is reserved for documentation, which is why this course uses it. "
            "Prefix math is about counting bits: a site receives a /48, and LAN segments are /64, so 64 minus 48 leaves 16 bits "
            "for subnet numbers, which is 65,536 subnets. Never squeeze a LAN smaller than /64; address autoconfiguration expects it."
        ),
        "assignment": "Submit lab_nif_ipv6_text JSON for NIF-5202: full, compressed, site_prefix_len, subnet_len, subnet_count.",
        "quiz": [
            ("What is the RFC 5952 form of 2001:0DB8:0000:0000:0001:0000:0000:0001?", ["2001:db8::1:0:0:1", "2001:db8:0:0:1::1", "2001:DB8::1::1", "2001:db8:0:0:1:0:0:1"], "first longest run"),
            ("When two zero runs are equally long, which one becomes ::?", ["The first", "The last", "Both", "Neither"], "tie rule"),
            ("Can :: replace a single all-zero group?", ["No", "Yes", "Only in uppercase", "Only at the end"], "two or more"),
            ("How many /64 subnets fit in a /48?", ["65,536", "16", "256", "4,096"], "2^16"),
            ("Which block is reserved for documentation?", ["2001:db8::/32", "2606:4700::/32", "fe80::/10", "::/0"], "RFC 3849"),
            ("Why keep LAN segments at /64?", ["Address autoconfiguration expects it", "It saves addresses", "It is faster", "Routers cannot route /64"], "SLAAC"),
        ],
    },
    {
        "title": "Bandwidth-delay product — why one connection cannot fill the pipe",
        "lab_id": "lab_nif_bdp_window",
        "worked_example": "1 Gbit/s × 0.080 s / 8 = 10,000,000 B BDP; 65,535-byte window × 8 / 0.080 s = 6.55 Mbit/s; window scale shift 8 (65,535 × 256 ≥ 10 MB)",
        "lesson": (
            "NIF-5303: a research group pays for a one-gigabit link to a partner 80 milliseconds away and complains that a "
            "single file transfer crawls at a few megabits. TCP may only have one window of unacknowledged bytes in flight, "
            "then must wait for acknowledgements to return. The bandwidth-delay product says how many bytes the pipe holds: "
            "one gigabit per second times 0.08 seconds is 80 million bits, or 10,000,000 bytes. The original TCP header "
            "allows a window of at most 65,535 bytes, so the sender stalls after 64 KiB each round trip; throughput is "
            "window times eight divided by the round-trip time, about 6.55 Mbit/s here, less than one percent of the link. "
            "RFC 7323 window scaling shifts the advertised window left by a negotiated count; a shift of 8 multiplies "
            "65,535 by 256 to about 16.8 MB, enough to cover the 10 MB product. The fix is end-host tuning and checking "
            "that no middlebox strips the option, not buying a bigger link."
        ),
        "assignment": "Submit lab_nif_bdp_window JSON for NIF-5303: rate_mbps, rtt_ms, window_bytes, bdp_bytes, max_throughput_mbps, window_scale_shift.",
        "quiz": [
            ("What is the BDP of 1 Gbit/s at 80 ms RTT?", ["10,000,000 bytes", "80,000,000 bytes", "65,535 bytes", "1,000,000 bytes"], "rate × RTT / 8"),
            ("A 65,535-byte window over 80 ms caps throughput at about?", ["6.55 Mbit/s", "1,000 Mbit/s", "65.5 Mbit/s", "0.8 Mbit/s"], "window×8/RTT"),
            ("Which window scale shift first covers a 10 MB BDP?", ["8", "4", "0", "14"], "65,535 × 256"),
            ("Why does buying a bigger link not fix NIF-5303?", ["The window, not the link, limits a single flow", "Links never help", "Latency doubles", "It costs nothing"], "window bound"),
            ("What can silently break window scaling?", ["A middlebox stripping the option", "IPv6", "Long passwords", "DNS"], "middlebox"),
            ("Doubling the RTT with a fixed window does what to throughput?", ["Halves it", "Doubles it", "No change", "Quadruples it"], "inverse"),
        ],
    },
    {
        "title": "BGP best path — policy first, then the shorter story",
        "lab_id": "lab_nif_bgp_path",
        "worked_example": "R1 lp100 [64500]; R2 lp200 len4 IGP; R3 lp200 len4 EGP → local_pref removes R1, AS_PATH ties, origin IGP<EGP → R2",
        "lesson": (
            "NIF-5404 asks why traffic to a partner network leaves through the long transit path instead of the direct one. "
            "Border Gateway Protocol routers hear several routes to the same prefix and pick one by walking an ordered list "
            "of attributes, stopping at the first that differs. This course uses a simplified order: highest local "
            "preference, shortest AS_PATH, lowest origin code with IGP before EGP before incomplete, lowest MED, then lowest "
            "router ID. Local preference is the operator's own policy, so it outranks everything about the route's length. "
            "Here R1 offers a one-hop path through documentation AS 64500 but carries local preference 100, while R2 and R3 "
            "both carry 200, so R1 is out at the first step even though its path is shortest. R2 and R3 each have four AS "
            "numbers, a tie, so the origin decides: R2 is IGP and R3 is EGP, and R2 wins. The deciding attribute is origin. "
            "Real routers add steps such as weight and eBGP-over-iBGP; RFC 4271 is the reference, and vendor documents list their full order."
        ),
        "assignment": "Submit lab_nif_bgp_path JSON for NIF-5404: best_route and deciding_attribute with a sentence per eliminated route.",
        "quiz": [
            ("Which attribute is compared first in the course's simplified order?", ["Local preference", "AS_PATH length", "MED", "Router ID"], "policy"),
            ("Why is R1 eliminated despite the shortest path?", ["Its local preference is lower", "Its router ID is high", "Its MED is zero", "It is EGP"], "lp 100 < 200"),
            ("R2 and R3 both have four-AS paths. What decides next?", ["Origin code", "Router ID", "Local preference again", "Path colour"], "next step"),
            ("Which origin code is preferred?", ["IGP", "EGP", "Incomplete", "All equal"], "lowest"),
            ("Which route wins NIF-5404?", ["R2", "R1", "R3", "None"], "origin IGP"),
            ("Where is the authoritative BGP specification?", ["RFC 4271", "RFC 5952", "RFC 1034", "RFC 7489"], "reference"),
        ],
    },
    {
        "title": "DNS TTL — planning a change the world sees late",
        "lab_id": "lab_nif_dns_ttl",
        "worked_example": "TTL 3600; resolver cached at t=3000 → expires 6600; record changed at 5000 → stale window 1600 s; worst case 3600 s; lower TTL by t=1400",
        "lesson": (
            "NIF-5505 is a cutover: a public website moves to new servers at t = 5,000 seconds and the old servers will be "
            "switched off soon after. Resolvers that looked up the name keep the answer for its time to live, and RFC 1034 "
            "lets them reuse it without asking again. A resolver that cached the record at t = 3,000 with a TTL of 3,600 "
            "seconds will hand out the old address until t = 6,600, so its users see the old site for 1,600 seconds after "
            "the change. In the worst case a resolver caches the old answer one second before the change and stays stale for "
            "the whole TTL, 3,600 seconds. The fix is planning: lower the TTL to something short, such as 300 seconds, at "
            "least one old TTL before the change, so by t = 1,400 at the latest, and raise it again once the new servers are "
            "stable. Keep the old servers answering until the worst-case window has passed. A change is not live when the "
            "zone file is saved; it is live when the last cache has expired."
        ),
        "assignment": "Submit lab_nif_dns_ttl JSON for NIF-5505: ttl_s, cached_at_s, changed_at_s, stale_until_s, stale_window_s, worst_case_s, lower_ttl_by_s.",
        "quiz": [
            ("Cached at 3,000 with TTL 3,600. When does that resolver's copy expire?", ["t = 6,600", "t = 3,600", "t = 5,000", "t = 8,600"], "cached + TTL"),
            ("The record changed at 5,000. How long does that resolver serve stale data?", ["1,600 seconds", "3,600 seconds", "0 seconds", "5,000 seconds"], "6,600 − 5,000"),
            ("What is the worst-case stale window for TTL 3,600?", ["3,600 seconds", "1,600 seconds", "300 seconds", "None"], "full TTL"),
            ("By when must the TTL be lowered for a change at 5,000?", ["t = 1,400", "t = 4,999", "t = 5,000", "t = 6,600"], "one TTL before"),
            ("When is a DNS change actually live everywhere?", ["When the last cache has expired", "When the zone is saved", "Immediately", "After a reboot"], "caches"),
            ("Why keep old servers answering after the change?", ["Stale resolvers still send users there", "For fun", "To double cost", "DNS requires it forever"], "overlap"),
        ],
    },
    {
        "title": "CDN offload — the miss ratio is what the origin pays for",
        "lab_id": "lab_nif_cdn_offload",
        "worked_example": "12,000 rps × 150 KB: hit 0.92 → 960 rps, 1.152 Gbit/s at origin; hit 0.96 → 480 rps, 0.576 Gbit/s; edge serves 14.4 Gbit/s total",
        "lesson": (
            "NIF-5606: a public broadcaster expects 12,000 requests per second for a live results page, each object about "
            "150 kilobytes, and its origin servers sit behind a two-gigabit link. A content delivery network answers from "
            "edge caches when it can, and only the misses travel back to the origin. The origin's load scales with the miss "
            "ratio, one minus the hit ratio. At a 92 percent hit ratio, 8 percent of 12,000 is 960 requests per second, and "
            "960 times 150,000 bytes times 8 bits is 1.152 gigabits per second, uncomfortably close to the two-gigabit "
            "link. Raising the hit ratio to 96 percent halves the misses to 480 requests per second and 0.576 Gbit/s. Four "
            "points of hit ratio halved the origin's work, which is why cache keys, longer TTLs for static images, and "
            "stripping needless query strings matter. The edge still delivers all 14.4 Gbit/s to viewers, so the CDN contract "
            "must cover that. Multiplying by the hit ratio instead of the miss ratio gives a number that looks impressive and is wrong."
        ),
        "assignment": "Submit lab_nif_cdn_offload JSON for NIF-5606: total_rps, object_kb, two scenarios with origin_rps and origin_gbps.",
        "quiz": [
            ("At a 92% hit ratio and 12,000 rps, how many requests reach the origin?", ["960 per second", "11,040 per second", "9,200 per second", "120 per second"], "miss × total"),
            ("What origin bandwidth do 960 rps of 150 KB objects need?", ["1.152 Gbit/s", "144 Mbit/s", "14.4 Gbit/s", "0.96 Gbit/s"], "×150,000×8"),
            ("Raising the hit ratio from 92% to 96% does what to origin load?", ["Halves it", "Cuts it by 4%", "Doubles it", "No change"], "8% → 4%"),
            ("Which ratio does origin load scale with?", ["The miss ratio", "The hit ratio", "The TTL", "The object count"], "1 − hit"),
            ("Total edge delivery for 12,000 rps of 150 KB is about?", ["14.4 Gbit/s", "1.44 Gbit/s", "144 Gbit/s", "1.152 Gbit/s"], "all requests"),
            ("Which change usually raises the hit ratio?", ["Stripping needless query strings from cache keys", "Shorter TTLs on images", "Disabling caching", "Adding random parameters"], "cache keys"),
        ],
    },
    {
        "title": "Optical link budget — loss, margin, and the 3 dB rule",
        "lab_id": "lab_nif_optical_budget",
        "worked_example": "40 km × 0.35 + 4 × 0.5 + 6 × 0.1 = 16.6 dB loss; margin = 0 − 16.6 − (−23) = 6.4 dB ≥ 3 → passes",
        "lesson": (
            "NIF-5707 is a NO_AI week: do the decibel arithmetic on paper first. A field team must confirm that optics with "
            "a 0 dBm transmitter and a receiver sensitivity of −23 dBm will work over a new 40 km span. Decibels add, which "
            "is why engineers like them. The planning coefficients are 0.35 dB per kilometre of fiber, 0.5 dB for each "
            "mated connector, and 0.1 dB for each fusion splice. Forty kilometres costs 14 dB, four connectors cost 2, and "
            "six splices cost 0.6, for 16.6 dB in total. The light arrives at −16.6 dBm, and the receiver can still read it "
            "down to −23, so the margin is 6.4 dB. The backbone rule asks for at least 3 dB of margin to cover ageing, "
            "dirty connectors, temperature, and the repair splices a backhoe will eventually require, so this span passes. "
            "Counting only fiber loss would claim 9 dB of margin and hide two decibels of connectors. Clean and inspect "
            "every connector before measuring, and compare the light meter's reading with the budget."
        ),
        "assignment": "Submit lab_nif_optical_budget JSON for NIF-5707 (NO_AI): km, connectors, splices, tx_dbm, rx_sens_dbm, loss_db, margin_db, passes.",
        "quiz": [
            ("What is the total loss for 40 km, 4 connectors, and 6 splices?", ["16.6 dB", "14.0 dB", "20.6 dB", "10.0 dB"], "sum"),
            ("With tx 0 dBm and sensitivity −23 dBm, what is the margin?", ["6.4 dB", "9.0 dB", "23 dB", "−6.4 dB"], "0 − 16.6 + 23"),
            ("Does the span pass the 3 dB rule?", ["Yes", "No", "Only at night", "Cannot tell"], "6.4 ≥ 3"),
            ("Why do engineers like decibels for budgets?", ["Losses add instead of multiply", "They are larger numbers", "They are metric", "They avoid physics"], "logarithms"),
            ("What does counting only fiber loss do?", ["Overstates the margin", "Understates the margin", "Nothing", "Fails every span"], "hidden loss"),
            ("What should happen before measuring with a light meter?", ["Clean and inspect every connector", "Bend the fiber", "Remove the splices", "Raise the transmitter"], "hygiene"),
        ],
    },
    {
        "title": "Availability — redundancy in parallel, single points in series",
        "lab_id": "lab_nif_availability",
        "worked_example": "pair 1 − (0.001 × 0.001) = 0.999999; × 0.9995 × 0.9999 = 0.9993991; downtime (1 − A) × 525,600 = 315.9 min/yr",
        "lesson": (
            "NIF-5808: a regional exchange's design has two core routers sharing traffic, each available 99.9 percent of "
            "the time, followed by one power feed at 99.95 percent and one fiber uplink at 99.99 percent. The question from "
            "management is how many minutes a year customers should expect to lose. A redundant pair fails only when both "
            "members are down at once, so its unavailability is the product of theirs: 0.001 times 0.001 is one in a "
            "million, making the pair 0.999999 available, assuming failures are independent. Parts in series all have to "
            "work, so their availabilities multiply: 0.999999 times 0.9995 times 0.9999 is about 0.9993991. A year has "
            "525,600 minutes, so expected downtime is about 315.9 minutes, more than five hours, almost all of it from the "
            "single power feed. Spending more on routers would barely move the result; a second feed would. Shared causes "
            "such as one power strip feeding both routers break the independence assumption and must be designed away."
        ),
        "assignment": "Submit lab_nif_availability JSON for NIF-5808: parallel_pair, serial, availability, downtime_min_per_year.",
        "quiz": [
            ("Two 99.9% routers in parallel give what availability?", ["0.999999", "0.998", "0.9999", "0.999"], "1 − 0.001²"),
            ("What happens to availability for parts in series?", ["They multiply", "They add", "The best one wins", "They average"], "all must work"),
            ("What is the design's overall availability?", ["About 0.9993991", "About 0.9984", "About 0.99999", "About 0.9999"], "product"),
            ("About how many minutes of downtime per year does it imply?", ["About 316", "About 841", "About 53", "About 5"], "× 525,600"),
            ("Which single change would help most?", ["A second power feed", "Faster routers", "More router RAM", "A new logo"], "weakest serial part"),
            ("What breaks the independence assumption?", ["Both routers on one power strip", "Different colours", "Separate racks", "Separate feeds"], "shared cause"),
        ],
    },
    {
        "title": "95th-percentile billing — the bursts you do not pay for",
        "lab_id": "lab_nif_p95_billing",
        "worked_example": "20 five-minute samples sorted; index ceil(0.95 × 20) − 1 = 18 → 720 Mbit/s × $0.35 = $252; the single 905 Mbit/s burst is free",
        "lesson": (
            "NIF-5909, the second NO_AI week, is a disputed transit invoice. Many internet transit contracts bill on the 95th "
            "percentile: the provider records average throughput every five minutes, sorts the month's samples, throws away "
            "the top five percent, and bills the highest remaining sample. The course fixture has twenty samples between "
            "289 and 905 Mbit/s. With twenty samples, five percent is one, so the bill uses the sample at sorted index "
            "ceil(0.95 × 20) − 1, which is index 18 counting from zero. Sorted, that is 720 Mbit/s, while the 905 Mbit/s "
            "burst at the top is discarded. At $0.35 per Mbit/s the charge is $252. Billing the peak would charge $316.75, "
            "and billing the mean would undercount the busy hours. A real month has about 8,640 samples, so roughly 432 "
            "five-minute periods, about 36 hours, can burst without raising the bill. Know where your provider samples, "
            "whether inbound and outbound are compared, and check their arithmetic before paying."
        ),
        "assignment": "Submit lab_nif_p95_billing JSON for NIF-5909 (NO_AI): samples_mbps, usd_per_mbps, p95_mbps, bill_usd, free_burst_samples.",
        "quiz": [
            ("With 20 samples, which sorted index (from zero) is billed?", ["18", "19", "20", "0"], "ceil(19) − 1"),
            ("What is the billed rate in the course fixture?", ["720 Mbit/s", "905 Mbit/s", "640 Mbit/s", "455 Mbit/s"], "index 18"),
            ("At $0.35 per Mbit/s, what is the charge?", ["$252", "$316.75", "$224", "$35"], "720 × 0.35"),
            ("How many samples are free bursts with 20 samples?", ["One", "Zero", "Two", "Five"], "5%"),
            ("Roughly how many hours of bursting does a 30-day month allow?", ["About 36", "About 3.6", "About 360", "None"], "432 × 5 min"),
            ("Why is billing the peak wrong under this contract?", ["The top 5% of samples are discarded", "Peaks are illegal", "Peaks are averages", "It is cheaper"], "contract"),
        ],
    },
    {
        "title": "Backbone design packet — documentation numbers, recomputed",
        "lab_id": "lab_nif_design_packet",
        "worked_example": "ASN 64500, prefix 2001:db8:4400::/48, 1,145 km → 5.6067 ms, availability 0.9993991 vs target 0.999 met, margin 6.4 dB, production_peering_claim false",
        "lesson": (
            "NIF-5A10 closes the term with a design packet for the regional backbone that the class has been building. It "
            "uses only documentation numbers: an autonomous system number from 64496 to 64511, here 64500, and an IPv6 "
            "prefix inside 2001:db8::/32, here 2001:db8:4400::/48. Using a real company's ASN or prefix in a training packet "
            "can leak into configurations and hijack someone else's traffic, so the reviewer rejects it on sight. The "
            "packet recomputes rather than restates: the 1,145 km route's propagation delay, the availability of the "
            "redundant core with its serial power feed and uplink compared with the 0.999 target, and the 6.4 dB optical "
            "margin. It cites RFC 4271, 5952, 7323, and 1034 for the behaviour it relies on. The final line says plainly "
            "that the packet is a classroom exercise and makes no claim about production peering or real customer service. "
            "Mentors pick one number at random and ask the author to derive it at the whiteboard."
        ),
        "assignment": "Submit lab_nif_design_packet JSON for NIF-5A10: labs_passed, asn, ipv6_prefix, recomputed latency/availability/optical, production_peering_claim false.",
        "quiz": [
            ("Which ASN range is reserved for documentation?", ["64496–64511", "13335–13350", "1–100", "65535 only"], "RFC 5398"),
            ("Why must training packets avoid real ASNs and prefixes?", ["They can leak into configs and hijack traffic", "They are too long", "They cost money", "They are secret"], "safety"),
            ("Does 0.9993991 meet a 0.999 target?", ["Yes", "No", "Only with RAID", "Cannot tell"], "compare"),
            ("What does 'recompute rather than restate' mean here?", ["Derive each number from its inputs", "Copy last term's figures", "Round everything to 1", "Skip the math"], "method"),
            ("What must the final line of the packet say?", ["No production peering claim", "Guaranteed uptime", "Certified by Cisco", "Live customer service"], "boundary"),
            ("How do mentors check the packet?", ["Ask the author to derive a random number at the whiteboard", "Check the font", "Count pages", "Accept it unread"], "oral check"),
        ],
    },
]

MID = [
    ("A 2,000 km fiber route with index 1.468 has about how much propagation delay?", ["About 9.8 ms", "About 6.7 ms", "About 20 ms", "About 2 ms"], "2,000 × 1.468 / 299,792"),
    ("A 9,000-byte jumbo frame at 10 Gbit/s takes how long to serialize?", ["7.2 µs", "72 µs", "0.9 µs", "720 µs"], "72,000 bits / 1e10"),
    ("Why can a satellite link never match a short fiber path's latency?", ["Propagation distance dominates", "Satellites are slow computers", "Packets are larger", "DNS is slower"], "physics"),
    ("A neighbour table lists the link-local address FE80:0000:0000:0000:0204:61FF:FE9D:F156. How should the change record write it?", ["fe80::204:61ff:fe9d:f156", "fe80::0204:61ff:fe9d:f156", "FE80::204:61FF:FE9D:F156", "fe80:0:0:0:204:61ff:fe9d:f156"], "lowercase, drop leading zeros, compress the zero run"),
    ("How many /56 prefixes fit in a /48?", ["256", "65,536", "8", "16"], "2^8"),
    ("What is the BDP of 100 Mbit/s at 40 ms RTT?", ["500,000 bytes", "4,000,000 bytes", "40,000 bytes", "100,000 bytes"], "1e8 × 0.04 / 8"),
    ("A transfer over 160 ms with a 65,535-byte window caps at about?", ["3.28 Mbit/s", "6.55 Mbit/s", "13.1 Mbit/s", "65.5 Mbit/s"], "window×8/0.16"),
    ("Two routes have equal local preference; one AS_PATH has 2 ASNs, the other 5. Which wins?", ["The 2-ASN route", "The 5-ASN route", "Lowest router ID", "Neither"], "shortest path"),
    ("An operator wants all traffic to prefer one upstream regardless of path length. Which attribute?", ["Higher local preference", "Lower MED", "Router ID", "Origin"], "policy"),
    ("A record with TTL 300 changes at t=10,000. Worst-case stale window?", ["300 seconds", "10,000 seconds", "0 seconds", "3,600 seconds"], "full TTL"),
    ("A migration is at t=86,400 and the current TTL is 86,400. By when must it be lowered?", ["t = 0", "t = 43,200", "t = 86,399", "t = 86,400"], "one TTL before"),
    ("At 8,000 rps and a 0.90 hit ratio, how many requests reach origin?", ["800 per second", "7,200 per second", "90 per second", "8,000 per second"], "miss × total"),
    ("800 rps of 200 KB objects need about how much origin bandwidth?", ["1.28 Gbit/s", "160 Mbit/s", "12.8 Gbit/s", "200 Mbit/s"], "800×200,000×8"),
    ("A 20 km span with 2 connectors and 4 splices has how much loss by the course coefficients?", ["8.4 dB", "7.0 dB", "10.0 dB", "4.4 dB"], "7 + 1 + 0.4"),
    ("Tx −3 dBm, loss 18 dB, sensitivity −20 dBm. Margin and verdict?", ["−1 dB, fails", "5 dB, passes", "3 dB, passes", "17 dB, passes"], "−3 − 18 + 20"),
    ("Two 99% links in parallel are available about how much?", ["99.99%", "98%", "99.5%", "100%"], "1 − 0.01²"),
    ("A 99.9% firewall in series with a 99.99% switch is available about how much?", ["99.89%", "99.99%", "99.95%", "100.89%"], "product"),
    ("What is 99.9% availability in downtime per year?", ["About 525.6 minutes", "About 52.6 minutes", "About 5.3 minutes", "About 8,760 minutes"], "0.001 × 525,600"),
    ("A month has 8,640 five-minute samples. How many are discarded at the 95th percentile?", ["432", "864", "43", "8,208"], "5%"),
    ("Why do providers sample in five-minute averages?", ["It smooths microbursts into a billable record", "It is the law", "It doubles bills", "Routers cannot count faster"], "billing method"),
]

FINAL = [
    ("A sales team promises 2 ms one-way across 1,145 km of fiber. What do you say?", ["Impossible; propagation alone is about 5.6 ms", "Fine with a faster router", "Possible on Sundays", "Only with IPv6"], "physics"),
    ("Upgrading a link from 1 to 10 Gbit/s reduces which part of a 1,145 km budget?", ["Serialization only", "Propagation", "Both by ten", "Neither"], "bits"),
    ("Two engineers write 2001:DB8:0:0:1::1 and 2001:db8::1:0:0:1 for the same address. Which is canonical?", ["2001:db8::1:0:0:1", "2001:DB8:0:0:1::1", "Both", "Neither"], "first longest run"),
    ("A customer asks for a /72 on a LAN to save space. Your answer?", ["Keep LANs at /64; autoconfiguration expects it", "Agree", "Use /128 everywhere", "Use IPv4"], "standard"),
    ("A long-haul transfer stalls at 6 Mbit/s on a 1 Gbit/s link. First check?", ["TCP window scaling on both hosts and middleboxes", "Buy 10 Gbit/s", "Change DNS", "Replace the fiber"], "BDP"),
    ("Why does a 200 ms path need a larger window than a 20 ms path at the same rate?", ["The bandwidth-delay product is ten times larger", "Packets are larger", "DNS is slower", "BGP prefers it"], "BDP"),
    ("A route has the shortest AS_PATH but loses. Most likely reason?", ["Another route has higher local preference", "Router IDs are random", "IPv6 broke it", "TTL expired"], "order"),
    ("Why is local preference above AS_PATH in the order?", ["It encodes the operator's own policy", "It is shorter", "It is newer", "It is random"], "policy"),
    ("A cutover is planned for tomorrow and the TTL is one day. What should you have done?", ["Lowered the TTL at least a day earlier", "Nothing", "Raised the TTL", "Deleted the record"], "planning"),
    ("Why keep old servers running after a DNS change?", ["Resolvers can serve the old answer for up to one TTL", "To test BGP", "For backups", "DNS changes are instant"], "overlap"),
    ("The origin link is near capacity at a 92% hit ratio. Highest-leverage fix?", ["Raise the hit ratio; misses drive origin load", "Lower the TTL", "Disable the CDN", "Add query strings"], "miss ratio"),
    ("A report says 'the CDN offloads 92%, so origin sees 11,040 rps of 12,000'. What is wrong?", ["It multiplied by the hit ratio instead of the miss ratio", "Nothing", "It should be 12,000", "It ignored DNS"], "miss ratio"),
    ("A span measures 4 dB worse than budget. Likely first cause?", ["Dirty or damaged connectors", "Wrong IPv6 prefix", "BGP origin", "DNS TTL"], "hygiene"),
    ("Why require 3 dB of optical margin?", ["Ageing, temperature, and repair splices add loss over time", "It looks tidy", "Receivers like round numbers", "It is the transmitter power"], "margin"),
    ("Both core routers share one power strip. What does that do to the availability estimate?", ["It is overstated; failures are not independent", "Nothing", "It improves", "It doubles"], "shared cause"),
    ("The serial power feed dominates downtime. Most effective investment?", ["A second independent feed", "Faster routers", "Larger optics", "A new website"], "weakest link"),
    ("A provider bills the month's peak sample under a 95th-percentile contract. What do you do?", ["Dispute it with the sorted samples and index", "Pay it", "Ignore it", "Switch to IPv6"], "contract"),
    ("Why does 95th-percentile billing reward scheduling backups at quiet times?", ["Short bursts in the top 5% are not billed", "Night traffic is free by law", "Backups are invisible", "It lowers latency"], "bursts"),
    ("A design packet uses AS 13335 and 2606:4700::/32. Verdict?", ["Reject; those are real allocations, not documentation", "Accept", "Accept if reviewed", "Accept with a footnote"], "documentation only"),
    ("Which statement belongs in every backbone design packet in this course?", ["No production peering claim", "Guaranteed five nines", "Certified CCNA design", "Live traffic carried"], "boundary"),
    ("Which public reference governs the TCP window scale option?", ["RFC 7323", "RFC 1034", "RFC 4271", "RFC 7489"], "window scaling"),
    ("Which use of Cisco CCNA material is acceptable here?", ["Topic labels only, no exam items", "Copying exam questions", "Selling vouchers", "Claiming certification"], "reference"),
    ("A packet restates last term's availability figure without inputs. What should the reviewer do?", ["Ask for the recomputation from inputs", "Accept it", "Round it up", "Delete the packet"], "recompute"),
    ("What does completing the Backbone Room course claim?", ["Infrastructure practice with recomputed labs, not a certification or production role", "CCNP certification", "ISP employment", "Peering authority"], "boundary"),
]
