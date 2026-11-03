"""IT_SUPPORT_HARDWARE — Refurb Bench. Authored week by week; numbers match batch009/labs_ish.py."""

COURSE_ID = "IT_SUPPORT_HARDWARE"
PREFIX = "ish"
TITLE = "IT Support and Hardware Foundations — Refurb Bench"
ACADEMY = "ACADEMY_IT"
KINESTHETIC = (
    "Ten Refurb Bench work orders on donated PCs: size the PSU → populate memory channels → plan RAID → choose MBR or GPT → "
    "isolate a fault → match display and cable → size a UPS → image a lab → sanitize drives → file the service report."
)
SYLLABUS_HOOK = (
    "IT_SUPPORT_HARDWARE COURSE_DIGITAL_RC: bench-technician arithmetic and decision tables for refurbishing donated "
    "computers — power budgets, memory channels, RAID, partition schemes, fault isolation, display bandwidth, UPS "
    "runtime, imaging throughput, and media sanitization. Distinct from GENERAL_IT (tickets and operating systems) and "
    "HARDWARE_ENGINEERING (circuits and embedded design). Not student/teacher E6."
)
CAREER = {
    "roles": ["it_support_technician_entry", "pc_refurbishment_technician", "deskside_support_apprentice"],
    "nice_categories": ["operate_and_maintain"],
    "certs_aligned_not_granted": [
        "CompTIA A+ hardware domain labels (PUBLIC_REFERENCE_ONLY; no exam items)",
        "NIST SP 800-88 media sanitization vocabulary (PUBLIC_REFERENCE_ONLY)",
        "UEFI specification boot vocabulary (PUBLIC_REFERENCE_ONLY)",
    ],
}
NO_AI_WEEKS = [3, 9]

WEEKS = [
    {
        "title": "Power supply budget — parts, headroom, and the smallest adequate unit",
        "lab_id": "lab_ish_psu_budget",
        "worked_example": "CPU 125 + GPU 200 + board 50 + RAM 10 + SSD 8 + fans 12 = 405 W × 1.25 = 506.25 W → 550 W unit",
        "lesson": (
            "Work order ISH-4101: a donated tower is getting a graphics card so a youth club can edit video, and the old 450 W "
            "power supply is suspect. Start with a parts list and each part's rated draw from its spec sheet, not from a "
            "forum guess. The processor is rated 125 W, the card 200 W, the motherboard about 50, two memory sticks about 10 "
            "together, the SSD about 8, and the fans about 12, for 405 W. A supply running near its limit gets hot, loud, and "
            "less efficient, and real loads spike above their averages, so the bench adds a quarter on top: 405 × 1.25 is "
            "506.25 W. The smallest catalogue unit that covers it is 550 W, so the 450 W supply goes in the parts bin. Bigger "
            "is not automatically better, since a 1,000 W unit idling at 60 W wastes money and often efficiency. Check that "
            "the new supply has the right connectors for the card, and never open a supply's case; the capacitors inside can "
            "hold a dangerous charge long after it is unplugged."
        ),
        "assignment": "Submit lab_ish_psu_budget JSON for ISH-4101: components, total_w, required_w, chosen_psu_w.",
        "quiz": [
            ("The parts total 405 W. What does the bench require after headroom?", ["506.25 W", "405 W", "450 W", "810 W"], "× 1.25"),
            ("Which catalogue unit should be chosen for 506.25 W?", ["550 W", "450 W", "850 W", "500 W"], "smallest adequate"),
            ("Why add headroom above the parts total?", ["Loads spike and supplies near their limit run hot", "Headroom is required by law", "To use more electricity", "Parts lie about colour"], "margin"),
            ("Where should a part's wattage come from?", ["Its spec sheet", "A forum guess", "Its colour", "The case size"], "source"),
            ("Why never open a power supply's case?", ["Capacitors can hold a dangerous charge after unplugging", "It voids the paint", "It is glued", "Fans fall out"], "safety"),
            ("Why is a 1,000 W unit a poor choice for a 300 W load?", ["It wastes money and may run less efficiently", "It will explode", "It cannot power fans", "It has no connectors"], "oversizing"),
        ],
    },
    {
        "title": "Memory channels — the slots you choose set the bandwidth",
        "lab_id": "lab_ish_memory_bandwidth",
        "worked_example": "DDR4-3200 in A2 + B2 → 2 channels → 3200 × 8 × 2 / 1000 = 51.2 GB/s; in A1 + A2 → 1 channel → 25.6 GB/s",
        "lesson": (
            "ISH-4202 is a slow machine that has two good memory sticks in it. Desktop boards usually have two memory "
            "channels, labelled A and B, each a separate 64-bit path to the processor. Each transfer moves eight bytes per "
            "channel, so peak bandwidth in gigabytes per second is the transfer rate in megatransfers per second times eight "
            "times the number of channels, divided by a thousand. DDR4-3200 in one channel gives 25.6 GB/s; spread across both "
            "channels it gives 51.2. The previous volunteer pushed both sticks into A1 and A2, which sit on the same channel, "
            "so the machine runs single-channel and integrated graphics, which borrow system memory, crawl. Moving one stick "
            "to B2 doubles the path without buying anything. The board manual names the preferred slots, often A2 and B2 for "
            "two sticks, and the firmware setup screen confirms the mode after a reboot. Handle sticks by the edges, match "
            "the notch to the key in the slot, and press until both latches click; a half-seated stick is a classic cause of "
            "beeps and no display."
        ),
        "assignment": "Submit lab_ish_memory_bandwidth JSON for ISH-4202: mt_s, slots_used, channels, bandwidth_gb_s.",
        "quiz": [
            ("DDR4-3200 in two channels gives what peak bandwidth?", ["51.2 GB/s", "25.6 GB/s", "3.2 GB/s", "102.4 GB/s"], "3200×8×2/1000"),
            ("Two sticks in A1 and A2 run how many channels?", ["One", "Two", "Four", "Zero"], "same letter"),
            ("Why did integrated graphics crawl on this machine?", ["They borrow system memory, which was single-channel", "The GPU was missing", "The sticks were too large", "The fans were slow"], "shared memory"),
            ("How many bytes move per channel per transfer?", ["Eight", "One", "Sixty-four", "Thirty-two"], "64-bit"),
            ("Where do you confirm the memory mode after a change?", ["The firmware setup screen", "The case sticker", "The keyboard", "The monitor menu"], "verify"),
            ("A half-seated stick commonly causes what?", ["Beeps and no display", "Faster boot", "Louder speakers", "Brighter screen"], "symptom"),
        ],
    },
    {
        "title": "RAID — usable space, tolerated failures, and why it is not a backup",
        "lab_id": "lab_ish_raid_capacity",
        "worked_example": "four 4 TB disks: RAID 0 16 TB/0, RAID 1 4 TB/3, RAID 5 12 TB/1, RAID 6 8 TB/2, RAID 10 8 TB/1 guaranteed",
        "lesson": (
            "ISH-4303 is a NO_AI week; build the table by hand. A community centre wants its donated four-bay storage box set "
            "up for shared files, with four 4 TB disks. RAID combines disks into one volume with different trade-offs. RAID 0 "
            "stripes data across all four for 16 TB and speed, but any single failure loses everything. RAID 1 mirrors the "
            "same data on every disk: only 4 TB usable, yet three disks can die. RAID 5 spreads one disk's worth of parity, "
            "leaving 12 TB and surviving one failure. RAID 6 uses two disks' worth of parity for 8 TB and survives any two. "
            "RAID 10 mirrors pairs and stripes across them, also 8 TB; it is guaranteed to survive one failure and survives a "
            "second only if it hits the other pair, so the honest table says one. With large disks, rebuilding after a failure "
            "takes many hours and stresses the survivors, which is why RAID 6 suits this box better than RAID 5. Most "
            "important: RAID protects against a disk dying, not against deletion, ransomware, or fire, because those damage "
            "every copy at once. The centre still needs the 3-2-1 backup plan."
        ),
        "assignment": "Submit lab_ish_raid_capacity JSON for ISH-4303 (NO_AI): disks, size_tb, five RAID levels, raid_is_backup false.",
        "quiz": [
            ("Four 4 TB disks in RAID 5 give how much usable space?", ["12 TB", "16 TB", "8 TB", "4 TB"], "n−1"),
            ("How many disk failures does RAID 6 survive guaranteed?", ["Two", "One", "Three", "None"], "double parity"),
            ("What does RAID 0 offer and risk?", ["Full capacity and speed; any failure loses all", "Mirroring and safety", "Parity protection", "Offsite copies"], "striping"),
            ("Why is RAID 10's guaranteed tolerance listed as one failure?", ["A second failure in the same mirror pair loses data", "It has no mirrors", "It uses parity", "It survives four failures"], "worst case"),
            ("Why is RAID not a backup?", ["Deletion and ransomware hit every disk at once", "It is too slow", "It needs four disks", "It is illegal"], "same volume"),
            ("Why prefer RAID 6 over RAID 5 with large disks?", ["Long rebuilds stress survivors; a second failure is survivable", "RAID 6 is faster always", "It uses fewer disks", "It needs no parity"], "rebuild risk"),
        ],
    },
    {
        "title": "MBR or GPT — the two-terabyte ceiling and UEFI boot",
        "lab_id": "lab_ish_partition_scheme",
        "worked_example": "MBR limit = 2^32 × 512 B = 2,199,023,255,552 B (2 TiB); 4 TB disk > limit → GPT, boot with UEFI; 4096-byte sectors raise the MBR limit to 16 TiB",
        "lesson": (
            "ISH-4404 is a new 4 TB data disk that shows only about 2 TB of usable space after the last technician set it up. "
            "A disk's partition table records where each partition starts and ends. The older Master Boot Record format "
            "stores those positions as 32-bit sector numbers, so it can address at most 2^32 sectors. With the common "
            "512-byte sectors that is 2,199,023,255,552 bytes, two tebibytes, and anything beyond is simply unreachable. "
            "The GUID Partition Table uses 64-bit addresses, supports far larger disks, keeps a backup copy of the table at "
            "the end of the disk, and allows many more partitions. A 4,000,000,000,000-byte disk is larger than the MBR "
            "ceiling, so it must be GPT. Disks with 4,096-byte native sectors stretch MBR to 16 TiB, but they are not what "
            "the bench usually sees. To boot an operating system from a GPT disk, the PC's firmware needs to run in UEFI "
            "mode rather than legacy BIOS mode, a setting in the firmware setup screen. Converting the scheme erases the "
            "table, so copy the data off and confirm the backup before you touch it."
        ),
        "assignment": "Submit lab_ish_partition_scheme JSON for ISH-4404: disk_bytes, sector_bytes, mbr_max_bytes, scheme, boot_firmware.",
        "quiz": [
            ("Why can MBR not address more than about 2 TiB with 512-byte sectors?", ["It stores sector numbers in 32 bits", "Disks are too slow", "It has no partitions", "It is encrypted"], "2^32"),
            ("What is the MBR limit in bytes with 512-byte sectors?", ["2,199,023,255,552", "2,000,000,000,000", "4,294,967,296", "512,000,000,000"], "2^32 × 512"),
            ("Which scheme must a 4 TB disk use to expose all of its space?", ["GPT", "MBR", "FAT", "Either"], "> limit"),
            ("What firmware mode boots an operating system from a GPT disk?", ["UEFI", "Legacy BIOS only", "Safe mode", "DOS"], "boot"),
            ("Where does GPT keep a backup copy of its table?", ["At the end of the disk", "In the BIOS chip", "In the cloud", "Nowhere"], "redundancy"),
            ("What must happen before converting a disk's partition scheme?", ["Copy the data off and confirm the backup", "Nothing", "Unplug the monitor", "Update the keyboard"], "data safety"),
        ],
    },
    {
        "title": "Fault isolation — symptom first, subsystem second, parts last",
        "lab_id": "lab_ish_fault_isolation",
        "worked_example": "T1 fans/no display/beeps → memory_or_cpu_seating; T2 dead → power_path; T3 shuts down under load → thermal_or_psu_capacity; T4 no boot device → boot_order_or_disk; T5 stop error after boot → driver_or_os",
        "lesson": (
            "ISH-4505 is five machines on the bench at once and a temptation to start swapping motherboards. Good technicians "
            "follow the power-on sequence, because each stage that succeeds rules out everything before it. No lights and "
            "no fans means the power path: the outlet, the cable, the supply's rear switch, then the supply itself. Fans "
            "spinning with beeps and no picture means the board is alive but the self-test failed, most often memory or a "
            "processor that is not seated; reseat the sticks one at a time before anything else. A self-test that passes "
            "and then complains there is no boot device points at the boot order in the firmware or a disk that is not "
            "detected. A machine that boots and then shows a stop error usually blames the last driver or update installed. "
            "Random shutdowns only under heavy load suggest heat or an undersized supply, so check temperatures and last "
            "week's power budget. Write down the symptom in the customer's words, the stage it fails at, and the cheapest "
            "test that would confirm your guess. Replacing parts before isolating the fault costs money and hides the real cause."
        ),
        "assignment": "Submit lab_ish_fault_isolation JSON for ISH-4505: classification of T1–T5 and replaced_parts_before_isolating false.",
        "quiz": [
            ("Fans spin, the PC beeps, and there is no display. First suspect?", ["Memory or CPU seating", "The monitor's brand", "The operating system", "The keyboard"], "POST failure"),
            ("No lights and no fans at all. Which path do you check first?", ["Power: outlet, cable, PSU switch", "Graphics driver", "Boot order", "RAM speed"], "power"),
            ("Self-test passes but 'no boot device' appears. What do you check?", ["Firmware boot order and disk detection", "PSU wattage", "Fan speed", "Monitor cable"], "boot"),
            ("A PC shuts down only during long renders. Likely cause?", ["Heat or an undersized power supply", "A bad mouse", "A missing driver for the printer", "The keyboard layout"], "load"),
            ("Why follow the power-on sequence?", ["Each passing stage rules out everything before it", "It is faster to guess", "Customers prefer it", "It voids warranties"], "isolation"),
            ("What does swapping parts before isolating usually cause?", ["Wasted money and a hidden real cause", "Faster fixes", "Better documentation", "Lower power use"], "shotgun"),
        ],
    },
    {
        "title": "Display bandwidth — will the cable carry the mode?",
        "lab_id": "lab_ish_display_link",
        "worked_example": "3840×2160×60×24 = 11.94 Gbit/s → fits HDMI 2.0 (14.4) and DP 1.4 (25.92), not HDMI 1.4 (8.16); at 120 Hz 23.89 Gbit/s → only DP 1.4",
        "lesson": (
            "ISH-4606: a donated 4K monitor flickers or drops to 30 Hz on a refurbished PC. A screen mode is a stream of "
            "pixels, and the cable has a ceiling. Multiply width by height by refresh rate by bits per pixel: 3,840 by 2,160 "
            "at 60 Hz with 24-bit colour is about 11.94 gigabits per second. That ignores the blanking intervals between "
            "lines and frames, so the true need is somewhat higher, and the honest label is lower bound. Compare it with "
            "each link's usable data rate after encoding overhead: HDMI 1.4 carries about 8.16, HDMI 2.0 about 14.4, and "
            "DisplayPort 1.4 about 25.92. The 4K 60 Hz mode fits HDMI 2.0 and DisplayPort 1.4 but not HDMI 1.4, which is why "
            "the old port falls back to 30 Hz. Double the refresh to 120 Hz and the need becomes about 23.89 Gbit/s, which "
            "only DisplayPort 1.4 carries uncompressed here. Cables and ports are both links in the chain: a certified "
            "high-speed cable on an old port still runs at the old port's speed, so read both before promising a customer "
            "a mode."
        ),
        "assignment": "Submit lab_ish_display_link JSON for ISH-4606: two modes with rate_gbps and fits per link, rate_is_lower_bound true.",
        "quiz": [
            ("What is the pixel data rate for 4K at 60 Hz and 24 bits per pixel?", ["About 11.94 Gbit/s", "About 23.89 Gbit/s", "About 8.16 Gbit/s", "About 1.5 Gbit/s"], "w×h×Hz×bpp"),
            ("Why is that figure a lower bound?", ["It ignores blanking intervals", "It includes audio", "Cables add speed", "It counts two monitors"], "blanking"),
            ("Which link cannot carry 4K 60 Hz uncompressed at 24-bit colour?", ["HDMI 1.4", "HDMI 2.0", "DisplayPort 1.4", "None of them"], "8.16 < 11.94"),
            ("Which link here carries 4K 120 Hz uncompressed?", ["DisplayPort 1.4", "HDMI 2.0", "HDMI 1.4", "VGA"], "25.92 > 23.89"),
            ("A new certified cable on an old HDMI 1.4 port runs at what speed?", ["The old port's speed", "Double speed", "DisplayPort speed", "Unlimited"], "weakest link"),
            ("Why does the old port fall back to 30 Hz?", ["Half the refresh fits under its ceiling", "30 Hz looks better", "The monitor is broken", "The OS prefers it"], "fallback"),
        ],
    },
    {
        "title": "UPS runtime — watt-hours, inverter loss, and a graceful shutdown",
        "lab_id": "lab_ish_ups_runtime",
        "worked_example": "864 Wh × 0.85 / 300 W × 60 = 146.9 min; start shutdown by 80% → no later than about 117 min (bench picks 110)",
        "lesson": (
            "ISH-4707: the community centre's storage box and router should ride out short power cuts and shut down cleanly "
            "during long ones. A battery's energy is in watt-hours, and the uninterruptible power supply converts it back to "
            "mains power through an inverter that loses some energy as heat. This unit holds two 12 V, 36 Ah batteries, "
            "about 864 Wh, and its inverter is about 85 percent efficient. The load measured at the wall is 300 W, so the "
            "runtime is 864 × 0.85 ÷ 300 hours, about 2.45 hours or 146.9 minutes. Batteries age, cold rooms reduce capacity, "
            "and the last minutes of a discharge are not reliable, so the bench starts a graceful shutdown no later than 80 "
            "percent of the computed runtime; here the plan picks 110 minutes. Configure the storage box to listen for the "
            "UPS's low-battery signal over USB or the network, and test it by pulling the plug while someone watches. Never "
            "plug a laser printer or a space heater into the battery outlets; their surges can overload the inverter."
        ),
        "assignment": "Submit lab_ish_ups_runtime JSON for ISH-4707: battery_wh, efficiency, load_w, runtime_min, shutdown_at_min.",
        "quiz": [
            ("864 Wh at 85% efficiency into a 300 W load lasts about how long?", ["146.9 minutes", "172.8 minutes", "86.4 minutes", "300 minutes"], "Wh×eff/W"),
            ("What does ignoring inverter efficiency do to the estimate?", ["Overstates the runtime", "Understates it", "Nothing", "Doubles the load"], "loss"),
            ("Why start shutdown by 80% of computed runtime?", ["Batteries age and the final minutes are unreliable", "To save paper", "It is faster", "UPS units require it by law"], "margin"),
            ("How does the storage box know to shut down?", ["It listens for the UPS low-battery signal", "Someone guesses", "It never shuts down", "The router tells it"], "signal"),
            ("Which device should not go on the battery outlets?", ["A laser printer", "The router", "The storage box", "The modem"], "surge"),
            ("How do you prove the shutdown works?", ["Pull the plug in a supervised test", "Assume it", "Read the box", "Ask the vendor"], "test"),
        ],
    },
    {
        "title": "Imaging a lab — unicast one by one versus one multicast stream",
        "lab_id": "lab_ish_imaging_time",
        "worked_example": "32 GB image × 8 = 256 Gbit ÷ (1 Gbit/s × 0.7) = 365.7 s per stream; 40 machines unicast ≈ 243.8 min; multicast ≈ 6.1 min",
        "lesson": (
            "ISH-4808: forty refurbished laptops need the same 32 GB system image before the library's coding club opens. "
            "Image sizes are in bytes and network links in bits, so start by multiplying by eight: 256 gigabits per copy. On a "
            "gigabit link that really delivers about 70 percent of its rating, one copy takes about 366 seconds, a little over "
            "six minutes. Sending the image to each laptop separately, unicast, repeats that forty times through the same "
            "server port: about 244 minutes, more than four hours. Multicast sends one stream that every listening machine "
            "receives together, so in the ideal case the whole lab finishes in about the time of a single copy, roughly six "
            "minutes. Real networks need switches that handle multicast properly, and one slow or faulty laptop can hold the "
            "session back, so plan a fallback to unicast for stragglers. Whatever the method, check one finished machine "
            "against a list of expected settings before releasing the rest, and record which image version went onto which "
            "serial numbers."
        ),
        "assignment": "Submit lab_ish_imaging_time JSON for ISH-4808: image_gb, machines, link_gbps, efficiency, unicast_min, multicast_min.",
        "quiz": [
            ("Why multiply the image size by eight first?", ["Images are in bytes, links in bits", "To add a safety margin", "Images compress by eight", "There are eight machines"], "units"),
            ("At 0.7 Gbit/s effective, how long is one 32 GB copy?", ["About 6.1 minutes", "About 32 seconds", "About 4 hours", "About 45 minutes"], "256/0.7 s"),
            ("Unicast to forty machines takes about how long?", ["About 244 minutes", "About 6 minutes", "About 40 seconds", "About 24 minutes"], "×40"),
            ("Why can multicast finish near the time of one copy?", ["Every machine receives the same single stream", "It compresses forty times", "It skips verification", "It uses Wi-Fi"], "one stream"),
            ("What should be ready if multicast stalls on a few laptops?", ["A unicast fallback for stragglers", "A new switch", "Nothing", "A second image"], "fallback"),
            ("What do you record after imaging?", ["Which image version went onto which serial numbers", "The weather", "Only the start time", "Nothing"], "traceability"),
        ],
    },
    {
        "title": "Media sanitization — Clear, Purge, or Destroy before a device leaves",
        "lab_id": "lab_ish_sanitize_decision",
        "worked_example": "RB-1001 HDD reuse_internal → Clear; RB-1002 SSD leave_org → Purge; RB-1003 failed SSD → Destroy; RB-1004 HDD leave_org → Purge; each verified with a certificate ID",
        "lesson": (
            "ISH-4909 is the second NO_AI week, because a sanitization decision has to be yours. Donated machines arrive "
            "full of strangers' lives, and the bench's promise is that nothing leaves with them. NIST Special Publication "
            "800-88 frames the choice with three words. Clear uses ordinary commands to overwrite user-addressable storage, "
            "enough when the device stays inside the organisation. Purge uses methods that defeat laboratory recovery, such "
            "as the drive's own secure-erase or cryptographic-erase commands, and is the floor when a device leaves your "
            "control through donation, sale, or a returned lease. Destroy means the media cannot be reused: shredding, "
            "disintegrating, or incinerating, and it is the only answer for a drive that has failed and will not accept "
            "commands. Solid-state drives remap blocks behind the scenes, so overwriting the visible space can leave old "
            "data in spare areas; rely on the drive's purge commands. Every decision ends with verification and a "
            "certificate recording the serial number, method, date, and who did it. A quick format is none of the three."
        ),
        "assignment": "Submit lab_ish_sanitize_decision JSON for ISH-4909 (NO_AI): method, verification, and certificate ID for RB-1001…1004.",
        "quiz": [
            ("A working SSD will be donated to another organisation. Minimum method?", ["Purge", "Clear", "Quick format", "None"], "leaves control"),
            ("A failed drive will not accept commands. What is left?", ["Destroy", "Clear", "Purge with software", "Reuse"], "only option"),
            ("Why is overwriting visible space risky on an SSD?", ["Remapped spare blocks can keep old data", "SSDs cannot be written", "It is too slow", "It voids the warranty"], "flash"),
            ("What fits a hard drive staying in the same organisation?", ["Clear", "Destroy", "Nothing", "Purge only by fire"], "internal reuse"),
            ("What must every sanitization end with?", ["Verification and a certificate", "A reboot", "A new label only", "A customer call"], "evidence"),
            ("Is a quick format Clear, Purge, or Destroy?", ["None of them", "Clear", "Purge", "Destroy"], "not sanitization"),
        ],
    },
    {
        "title": "Refurb service report — fault, fix, sanitization, proof",
        "lab_id": "lab_ish_service_report",
        "worked_example": "RB-1002: fault memory_or_cpu_seating, fix reseated DIMM in A2, sanitization Purge, verified; customer_data_retained false",
        "lesson": (
            "ISH-4A10 closes the term with the document that travels with each refurbished machine. For every device the "
            "report gives the serial number, the fault class from the bench's isolation table, and the fix in plain words, "
            "such as reseated the memory stick in A2. It records the sanitization method chosen for the drive and that "
            "verification passed, pointing at last week's certificate. It notes anything a new owner should know, like a "
            "replacement power supply, the memory mode confirmed in firmware, or a monitor that needs the DisplayPort cable "
            "for full refresh. The bench also signs one sentence for the whole batch: no customer data was retained, "
            "copied, or looked through beyond what the repair required. Technicians who browse a donor's photos to 'test the "
            "drive' end their volunteering that day. Mentors review the report against six or more passed labs, pick one "
            "machine at random, and ask the technician to explain the fault and the fix while the case is open. A clean "
            "report is what lets a school trust a donated computer."
        ),
        "assignment": "Submit lab_ish_service_report JSON for ISH-4A10: labs_passed, per-device fault/fix/sanitization/verification, customer_data_retained false.",
        "quiz": [
            ("Which field connects a device to its isolation work?", ["The fault class from the bench table", "The case colour", "The donor's name", "The price"], "fault class"),
            ("What must the report say about sanitization?", ["The method used and that verification passed", "Nothing", "Only the date", "The donor's address"], "proof"),
            ("A technician browses a donor's photos 'to test the drive'. What follows?", ["Their volunteering ends that day", "A thank-you note", "Nothing", "A promotion"], "privacy"),
            ("What should a new owner learn from the report?", ["Notable replacements and settings, like the cable for full refresh", "The donor's history", "Every quiz score", "Nothing"], "handover"),
            ("During review a mentor picks one machine and asks for what?", ["An explanation of the fault and fix with the case open", "A sales pitch", "A new image", "The donor's password"], "oral check"),
            ("What does a clean report let a school do?", ["Trust a donated computer", "Skip updates", "Ignore sanitization", "Avoid backups"], "trust"),
        ],
    },
]

MID = [
    ("A build totals 520 W of parts. Which supply does the bench rule pick?", ["650 W", "550 W", "750 W", "500 W"], "520 × 1.25 = 650 W exactly"),
    ("Why might a supply that meets the total still fail under a new graphics card?", ["It lacks the card's power connectors or rail capacity", "Supplies hate graphics", "Fans block it", "The case is too big"], "connectors"),
    ("Four sticks fill A1, A2, B1, B2. How many channels run?", ["Two", "Four", "One", "Eight"], "two letters"),
    ("DDR5-4800 in two channels gives what peak bandwidth by the bench formula?", ["76.8 GB/s", "38.4 GB/s", "4.8 GB/s", "153.6 GB/s"], "4800×8×2/1000"),
    ("Integrated graphics are slow and one stick is installed. Cheapest improvement?", ["Add a matching stick in the other channel", "Buy a new CPU", "Replace the case", "Lower the resolution to 640×480"], "dual channel"),
    ("Six 2 TB disks in RAID 6 give how much usable space?", ["8 TB", "10 TB", "12 TB", "6 TB"], "(n−2)×s"),
    ("A teacher deletes a folder on a RAID 1 volume. What happens on the mirror?", ["It is deleted there too", "It is kept safe", "It is restored automatically", "It moves to the cloud"], "not backup"),
    ("Why does a RAID 5 rebuild worry technicians with large disks?", ["Long rebuilds stress the remaining disks", "It deletes parity", "It shrinks capacity", "It is instant"], "risk window"),
    ("A 3 TB disk set up as MBR with 512-byte sectors exposes about how much?", ["About 2 TiB", "All 3 TB", "1 TB", "Nothing"], "ceiling"),
    ("A PC will not boot from a GPT disk after cloning. Which firmware setting do you check?", ["UEFI versus legacy BIOS mode", "Fan curve", "Keyboard layout", "Screen brightness"], "boot mode"),
    ("A machine is dead after a storm. What do you test before opening the case?", ["The outlet and power cable", "The graphics driver", "The RAM timings", "The boot order"], "cheapest first"),
    ("The PC boots, then shows a stop error right after a driver update. First step?", ["Roll back the last driver or update", "Replace the motherboard", "Reseat the CPU", "Change the PSU"], "recent change"),
    ("Why write the symptom in the customer's own words?", ["It preserves details your guess might discard", "Customers prefer it", "It is required by law", "It is shorter"], "evidence"),
    ("2560×1440 at 144 Hz with 24-bit colour needs about how much?", ["About 12.7 Gbit/s", "About 5.3 Gbit/s", "About 25 Gbit/s", "About 1.4 Gbit/s"], "2560×1440×144×24"),
    ("A monitor runs 4K at 30 Hz over HDMI 1.4. What is the honest fix?", ["Use a port and cable rated for the mode, like DP 1.4", "Buy a longer cable", "Lower the brightness", "Install a new keyboard"], "link"),
    ("A 600 Wh UPS at 90% efficiency feeds 180 W. Runtime?", ["180 minutes", "200 minutes", "120 minutes", "300 minutes"], "600×0.9/180 h"),
    ("Doubling the load on a UPS does what to runtime by the bench formula?", ["Halves it", "Doubles it", "No change", "Quarters it"], "inverse"),
    ("A 20 GB image goes to 10 machines over 1 Gbit/s at 80% efficiency, unicast. About how long?", ["About 33 minutes", "About 3.3 minutes", "About 200 minutes", "About 20 minutes"], "160/0.8 s ×10"),
    ("Why verify one finished machine before releasing an imaged lab?", ["One mistake would otherwise repeat on every machine", "It is tradition", "Imaging is random", "To slow down"], "batch error"),
    ("A leased laptop goes back to the vendor. Which category applies at minimum?", ["Purge", "Clear", "No action", "Quick format"], "leaves control"),
]

FINAL = [
    ("A volunteer wants a 1,200 W supply 'to be safe' for a 250 W office PC. Your advice?", ["Size to the budget with headroom; oversizing wastes money and efficiency", "Agree", "Use 300 W with no headroom", "Remove the fans"], "right-size"),
    ("A PSU's fan has stopped and it smells hot. What do you do?", ["Replace the unit; never open it", "Open it and clean the capacitors", "Tape the fan", "Run it at night only"], "safety"),
    ("A board manual says use A2 and B2 for two sticks, but they sit in A1 and B1. Likely effect?", ["Possibly unstable or not running the preferred layout; follow the manual", "Triple speed", "No display ever", "Nothing could matter"], "manual"),
    ("A customer asks why a gaming laptop with one stick has poor frame rates. Best explanation?", ["Single-channel memory halves bandwidth for integrated graphics", "The screen is too bright", "The keyboard is slow", "Batteries limit frames"], "channels"),
    ("A nonprofit wants maximum space on four disks for a scratch volume it can afford to lose. Which RAID?", ["RAID 0", "RAID 6", "RAID 1", "RAID 10"], "capacity"),
    ("A file server has RAID 6 and no other copy. Ransomware encrypts the share. What protects them?", ["Nothing, unless a separate backup exists", "RAID 6 parity", "The second parity disk", "The rebuild"], "backup"),
    ("A customer's 6 TB disk shows only 2 TB. What do you explain?", ["MBR cannot address beyond 2 TiB with 512-byte sectors; GPT is needed", "The disk is fake", "Windows hides 4 TB", "Cables limit size"], "ceiling"),
    ("Why keep a GPT disk's backup table in mind during recovery?", ["A damaged primary table can be rebuilt from it", "It stores passwords", "It doubles capacity", "It boots faster"], "resilience"),
    ("Five tickets arrive. Which practice keeps diagnosis honest?", ["Record the stage of failure and the cheapest confirming test", "Swap the motherboard first", "Guess from the case colour", "Reinstall the OS on all five"], "method"),
    ("A PC shuts down during games after a GPU upgrade but the CPU is cool. Next check?", ["The power budget against the new card", "Keyboard drivers", "Monitor size", "Mouse DPI"], "PSU"),
    ("A customer wants 4K 120 Hz on a PC with only HDMI 2.0. What do you say?", ["The port cannot carry it uncompressed; use DP 1.4 or accept 60 Hz", "Buy a gold cable", "It works fine", "Use VGA"], "honest limits"),
    ("Why label display rates as lower bounds?", ["Blanking intervals add to the real requirement", "Cables are faster than advertised", "Monitors round down", "It is tradition"], "blanking"),
    ("A UPS test lasts 40 minutes instead of the computed 60. What is the likely reason?", ["Aged batteries or a heavier load than measured", "The formula is wrong forever", "The UPS is too new", "The room is too quiet"], "real world"),
    ("A UPS feeds a router, a storage box, and a space heater. What must change?", ["Remove the heater from the battery outlets", "Add another heater", "Nothing", "Unplug the router"], "load"),
    ("Imaging forty machines by unicast takes four hours. Which change helps most?", ["Multicast with a unicast fallback", "Faster keyboards", "Larger monitors", "Imaging at night only"], "throughput"),
    ("The effective link rate halves from 0.7 to 0.35 Gbit/s. What happens to imaging time?", ["It doubles", "It halves", "No change", "It quadruples"], "inverse"),
    ("Which record should follow every imaged machine?", ["Image version and serial number", "The technician's playlist", "Nothing", "The donor's browsing history"], "traceability"),
    ("A donated SSD is going to a school. Which method satisfies the bench rule?", ["Purge using the drive's secure or cryptographic erase", "Delete files", "Quick format", "Rename the volume"], "purge"),
    ("A drive is physically cracked and spins noisily. Its sanitization?", ["Destroy", "Clear", "Purge by overwrite", "Reuse"], "failed media"),
    ("What belongs on a sanitization certificate?", ["Serial, method, date, and who did it", "The donor's photos", "The asking price", "Nothing"], "certificate"),
    ("A service report says 'fixed it'. What is missing?", ["Fault class, the specific fix, and sanitization proof", "Nothing", "A joke", "The donor's address"], "detail"),
    ("A technician copies a donor's music 'because it was good'. What rule was broken?", ["No customer data retained or copied", "Imaging rules", "RAID rules", "UPS rules"], "privacy"),
    ("Which CompTIA A+ use is acceptable in this course?", ["Domain labels for topics, no exam items", "Copying exam questions", "Selling vouchers", "Claiming certification"], "reference"),
    ("What does completing the Refurb Bench course claim?", ["Bench practice with recomputed labs, not a certification", "A+ certification", "Electrician licence", "Manufacturer warranty authority"], "boundary"),
]
