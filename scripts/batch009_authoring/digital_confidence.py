"""DIGITAL_CONFIDENCE — Library Lab. Authored week by week; numbers match batch009/labs_dco.py."""

COURSE_ID = "DIGITAL_CONFIDENCE"
PREFIX = "dco"
TITLE = "Digital Confidence to Computer Operator — Library Lab"
ACADEMY = "ACADEMY_IT"
KINESTHETIC = (
    "Ten Library Lab help-desk cards: find the file → read the drive label → judge a password → read a link → "
    "build a budget sheet → measure typing → fit an attachment → plan backups → check screen contrast → write a safety plan."
)
SYLLABUS_HOOK = (
    "DIGITAL_CONFIDENCE COURSE_DIGITAL_RC: first-computer confidence for adult and teen learners at a library lab — "
    "paths and folders, storage units, password strength, link reading, spreadsheet formulas, keyboard fluency, "
    "attachments, 3-2-1 backups, and readable screens. Practice data only. Distinct from GENERAL_IT, which trains "
    "support specialists. Not student/teacher E6."
)
CAREER = {
    "roles": ["computer_operator_entry", "library_digital_navigator_volunteer", "office_assistant_digital"],
    "nice_categories": ["operate_and_maintain"],
    "certs_aligned_not_granted": [
        "NIST SP 800-63B password guidance (PUBLIC_REFERENCE_ONLY)",
        "W3C WCAG 2.2 contrast criteria (PUBLIC_REFERENCE_ONLY)",
        "CISA Secure Our World habits (PUBLIC_REFERENCE_ONLY)",
    ],
}
NO_AI_WEEKS = [2, 6]

WEEKS = [
    {
        "title": "Folders and paths — knowing where a file really lives",
        "lab_id": "lab_dco_paths",
        "worked_example": "cwd /home/ana/Documents/letters + ../photos/2026/../summer.jpg → /home/ana/Documents/photos/summer.jpg",
        "lesson": (
            "Help card DCO-3101: Ana saved a summer photo and the file dialog now says 'not found'. Every file has an address "
            "called a path, written from the top of the drive down through folders, like /home/ana/Documents/photos/summer.jpg. "
            "That full form is an absolute path because it starts at the root, the single slash. Programs also accept relative "
            "paths that start from wherever you are standing, called the current working directory. Two dots mean the folder "
            "above, and a single dot means here. Standing in /home/ana/Documents/letters, the relative path "
            "../photos/2026/../summer.jpg climbs out of letters into Documents, steps into photos and into 2026, then climbs "
            "back out of 2026, landing on /home/ana/Documents/photos/summer.jpg. Walk it with your finger on a drawn tree "
            "before trusting it. Windows writes C:\\Users\\Ana\\Documents with backslashes and a drive letter, but the idea of "
            "climbing and descending is the same. When a file goes missing, ask two questions out loud: where am I standing, "
            "and which way does the path walk from here."
        ),
        "assignment": "Submit lab_dco_paths JSON for DCO-3101: two tasks with cwd, relative path, and resolved absolute path.",
        "quiz": [
            ("What does '..' mean in a path?", ["The folder above the current one", "The current folder", "The home folder", "A hidden file"], "parent"),
            ("Which path is absolute on Linux or macOS?", ["/home/ana/Documents", "Documents/letters", "../photos", "./form.pdf"], "starts at root"),
            ("From /home/ana, where does ./Downloads/form.pdf point?", ["/home/ana/Downloads/form.pdf", "/Downloads/form.pdf", "/home/Downloads/form.pdf", "/home/ana/form.pdf"], "dot = here"),
            ("Standing in /home/ana/Documents/letters, where does ../photos lead?", ["/home/ana/Documents/photos", "/home/ana/photos", "/photos", "/home/ana/Documents/letters/photos"], "one level up"),
            ("What should you ask first when a file 'disappears'?", ["Where am I standing, and which way does the path walk?", "Is the computer broken?", "Should I reinstall?", "Who deleted it?"], "orientation"),
            ("How does Windows usually separate folders in a path?", ["With backslashes after a drive letter", "With commas", "With spaces", "With dots only"], "C:\\"),
        ],
    },
    {
        "title": "Storage units — why a 500 GB drive shows 465 GiB",
        "lab_id": "lab_dco_storage_units",
        "worked_example": "500 GB = 500×10^9 B = 465.66 GiB; 1,200 photos × 4.2 MB = 5.04×10^9 B = 4.694 GiB > 4.5 GiB free → does not fit",
        "lesson": (
            "DCO-3202 is a NO_AI week; work the division on paper. A patron bought a '500 GB' drive and thinks the store cheated "
            "her because the computer shows about 465 GB. Nobody cheated. Drive makers count in powers of ten, so a gigabyte "
            "is 1,000,000,000 bytes. Many operating systems count in powers of two, where a gibibyte, GiB, is 1,073,741,824 "
            "bytes, and then label the result GB anyway. Divide 500,000,000,000 by 1,073,741,824 and you get about 465.66, "
            "the same drive described in a bigger unit. The same confusion bites when deciding whether something will fit. "
            "Her phone holds 1,200 photos at about 4.2 MB each, where MB means a million bytes, so the folder is 5.04 billion "
            "bytes. In the binary unit that is about 4.69 GiB, and the laptop says 4.5 GiB free. It will not fit, even though "
            "'5 GB into 4.5' felt close. Write the unit beside every number, convert both sides to the same unit before "
            "comparing, and leave room to spare, because a completely full disk makes most computers slow and unstable."
        ),
        "assignment": "Submit lab_dco_storage_units JSON for DCO-3202 (NO_AI): drive and photo sizes in GiB and the fit decision.",
        "quiz": [
            ("How many bytes are in a decimal gigabyte?", ["1,000,000,000", "1,073,741,824", "1,024,000", "8,000,000,000"], "10^9"),
            ("About how many GiB is a 500 GB drive?", ["465.66", "500", "512", "476.8"], "÷ 2^30"),
            ("Why did the store not cheat the patron?", ["The same bytes are counted in a larger unit", "Drives shrink with age", "The operating system steals space", "Labels are always wrong"], "units"),
            ("Twelve hundred photos at 4.2 MB each total about how many GiB?", ["4.69", "5.04", "4.20", "50.4"], "5.04e9 / 2^30"),
            ("4.69 GiB of photos, 4.5 GiB free. Does it fit?", ["No", "Yes", "Only on Tuesdays", "Only compressed by the OS automatically"], "compare same unit"),
            ("Why leave spare space on a disk?", ["A full disk makes most computers slow and unstable", "It wastes money", "Space expires", "It is required by law"], "headroom"),
        ],
    },
    {
        "title": "Passwords and passphrases — strength is length times choice",
        "lab_id": "lab_dco_entropy",
        "worked_example": "4 diceware words: 4×log2(7776) = 51.70 bits; 8 random printable: 8×log2(95) = 52.56; 12 random lowercase: 12×log2(26) = 56.41",
        "lesson": (
            "DCO-3303 starts with a sticky note that says P@ssw0rd! and a question: is this strong? Strength depends on how "
            "the password was chosen, not on how it looks. If every character is picked at random from a pool, the number of "
            "possibilities is the pool size raised to the length, and we measure it in bits: length times log2 of the pool. "
            "Four words drawn at random from a 7,776-word dice list give about 51.7 bits. Eight characters drawn at random "
            "from the 95 printable keyboard symbols give about 52.6 bits. Twelve random lowercase letters give about 56.4 "
            "bits, stronger than either, because length grows strength faster than adding symbols. P@ssw0rd! scores far "
            "lower than its nine characters suggest, because guessing tools try dictionary words with common swaps first. "
            "The NIST digital identity guidance, SP 800-63B, favours long memorable secrets, checking them against lists "
            "of known-breached passwords, and changing them when there is evidence of compromise rather than on a fixed "
            "calendar. Use a different secret on every site, and let a password manager remember them."
        ),
        "assignment": "Submit lab_dco_entropy JSON for DCO-3303: three schemes with pool, length, bits, the strongest, and the two policy flags.",
        "quiz": [
            ("How are password bits computed for random choices?", ["Length × log2(pool size)", "Pool size + length", "Number of symbols × 10", "Length squared"], "entropy"),
            ("Which is strongest among the three examples?", ["Twelve random lowercase letters", "Four diceware words", "Eight random printable characters", "P@ssw0rd!"], "56.4 bits"),
            ("Why is P@ssw0rd! weak despite symbols?", ["Guessers try dictionary words with common swaps first", "It is too long", "Symbols are illegal", "It has no spaces"], "not random"),
            ("What does NIST SP 800-63B say about forced periodic changes?", ["Change on evidence of compromise, not a fixed calendar", "Change every week", "Never change passwords", "Change on birthdays"], "rotation"),
            ("Why use a password manager?", ["It lets you keep a different secret on every site", "It makes passwords shorter", "It shares passwords with friends", "It removes the need for any password"], "uniqueness"),
            ("Adding one random word to a four-word diceware phrase adds about how many bits?", ["About 12.9", "About 1", "About 51.7", "Exactly 100"], "log2 7776"),
        ],
    },
    {
        "title": "Reading a link — the real address is at the right end",
        "lab_id": "lab_dco_link_check",
        "worked_example": "https://account.harborbank.example.verify-login.example.net/session → hostname ends in example.net → not harborbank.example → do not open",
        "lesson": (
            "DCO-3404 is a text message that says a bank account is locked and offers a link. Before tapping, read the address "
            "the way a computer does. Skip the https:// and stop at the first single slash after it; what sits between is "
            "the hostname. Read the hostname from the right end, label by label, because the rightmost labels say who owns "
            "it. In https://account.harborbank.example.verify-login.example.net/session the hostname is "
            "account.harborbank.example.verify-login.example.net, and its last two labels are example.net. The bank's name "
            "near the left is just decoration chosen by whoever owns example.net, which is not the bank. So the call is: do "
            "not open. Real organisations rarely ask you to log in from a message; type the bank's address yourself or use "
            "its app. Some country endings use three labels, such as .co.uk, so the rule 'last two labels' is a starting "
            "point, and the course's examples use the reserved .example endings so nobody is sent anywhere real. When unsure, "
            "show the message to the library desk rather than replying."
        ),
        "assignment": "Submit lab_dco_link_check JSON for DCO-3404: hostname, registered domain, and the safe_to_open decision.",
        "quiz": [
            ("Where does the hostname end in a web address?", ["At the first single slash after https://", "At the first dot", "At the end of the line", "At the word 'login'"], "host boundary"),
            ("From which end do you read a hostname to find its owner?", ["The right end", "The left end", "The middle", "Any end"], "right to left"),
            ("Who owns account.harborbank.example.verify-login.example.net?", ["Whoever owns example.net", "Harbor Bank", "The phone company", "Nobody"], "registered domain"),
            ("A message asks you to log in through its link. Safer choice?", ["Type the organisation's address yourself or use its app", "Tap quickly before it expires", "Reply with your password", "Forward it to friends"], "out-of-band"),
            ("Why does 'last two labels' need care for .co.uk addresses?", ["Some endings use three labels", "UK addresses are illegal", "Dots mean nothing", "It always works"], "public suffix"),
            ("Why do course links end in .example?", ["The ending is reserved, so nobody is sent anywhere real", "It is faster", "It is a bank", "It is encrypted"], "reserved"),
        ],
    },
    {
        "title": "Spreadsheet formulas — let the sheet do the arithmetic",
        "lab_id": "lab_dco_sheet_formulas",
        "worked_example": "rent 650, food 240, bus pass 55, phone 35, savings 120 → =SUM 1100, =AVERAGE 220, =MAX rent, food share =240/1100 = 21.82%",
        "lesson": (
            "DCO-3505 is a monthly budget written on the back of an envelope that never adds up the same way twice. Move it into "
            "a spreadsheet: labels in column A, amounts in column B, one row per item. Rent is 650, food 240, the bus pass 55, "
            "the phone 35, and savings 120. Instead of typing the total, write =SUM(B2:B6) and the sheet answers 1,100, then "
            "keeps answering correctly when the phone bill changes. =AVERAGE(B2:B6) gives 220, the typical line, and "
            "=MAX(B2:B6) finds the largest amount, which belongs to rent. To see how much of the month food takes, divide its "
            "cell by the total cell, =B3/B7, and format the result as a percentage: about 21.82 percent. The habit worth "
            "keeping is that numbers you typed live in one place and every other number is a formula pointing at them. A "
            "total typed by hand goes stale the first time anything changes, and that is how budgets quietly stop matching "
            "reality. Save the file somewhere you will find it, with a name that says what and when."
        ),
        "assignment": "Submit lab_dco_sheet_formulas JSON for DCO-3505: rows, total, average, largest item, and one share percentage.",
        "quiz": [
            ("What does =SUM(B2:B6) return for this budget?", ["1,100", "220", "650", "5"], "sum"),
            ("Why use a formula instead of typing the total?", ["It stays correct when a row changes", "It looks nicer", "Typing is forbidden", "Formulas are faster to print"], "single source"),
            ("What is food's share of the 1,100 total?", ["About 21.82%", "About 24%", "About 2.4%", "About 45%"], "240/1100"),
            ("Which function finds the largest amount?", ["MAX", "MIN", "COUNT", "AVERAGE"], "MAX"),
            ("What does =AVERAGE(B2:B6) give here?", ["220", "1,100", "240", "130"], "1100/5"),
            ("What is the habit this week builds?", ["Typed inputs in one place, everything else a formula", "Retype totals daily", "Avoid spreadsheets", "Use only percentages"], "habit"),
        ],
    },
    {
        "title": "Keyboard fluency — gross speed, net speed, accuracy",
        "lab_id": "lab_dco_typing_wpm",
        "worked_example": "1,250 characters in 5 minutes with 15 uncorrected errors → gross 50 WPM, net 47 WPM, accuracy 98.8%",
        "lesson": (
            "DCO-3606 is a NO_AI week because it measures your own hands. Job applications and online forms reward people who "
            "can type steadily, so the library runs a five-minute practice passage. Typing speed is counted in words per "
            "minute, where a 'word' is defined as five characters, spaces included, so long and short words count fairly. "
            "Typing 1,250 characters in five minutes is 250 'words' over five minutes, a gross speed of 50 WPM. Mistakes left "
            "uncorrected are subtracted per minute: fifteen errors over five minutes costs three, so net speed is 47 WPM. "
            "Accuracy compares correct characters with all characters, 1,235 out of 1,250, or 98.8 percent. Most learners "
            "improve fastest by slowing down until accuracy stays near ninety-eight percent, then letting speed return, "
            "because unlearning a mistyped pattern takes longer than learning it right. Sit square to the keyboard, keep "
            "wrists level, and rest the index fingers on the small bumps on F and J. Record the three numbers each week "
            "rather than chasing a single best run."
        ),
        "assignment": "Submit lab_dco_typing_wpm JSON for DCO-3606 (NO_AI): chars, minutes, errors, gross_wpm, net_wpm, accuracy_pct.",
        "quiz": [
            ("How many characters count as one word in WPM?", ["Five", "One", "Ten", "However many letters the word has"], "convention"),
            ("1,250 characters in 5 minutes is what gross speed?", ["50 WPM", "250 WPM", "25 WPM", "1,250 WPM"], "1250/5/5"),
            ("Fifteen uncorrected errors in five minutes reduce net speed by how much?", ["3 WPM", "15 WPM", "5 WPM", "0.3 WPM"], "per minute"),
            ("What is the accuracy for 15 errors in 1,250 characters?", ["98.8%", "85%", "99.9%", "95%"], "1235/1250"),
            ("Which practice habit improves speed fastest for most learners?", ["Slow down until accuracy holds near 98%", "Type as fast as possible always", "Never correct errors", "Look only at the keys"], "accuracy first"),
            ("Which keys have small bumps for the index fingers?", ["F and J", "A and L", "Q and P", "Enter and Space"], "home row"),
        ],
    },
    {
        "title": "Attachments — why a 19 MB file will not fit under 25 MB",
        "lab_id": "lab_dco_attachment_fit",
        "worked_example": "19,000,000 B → base64 4·ceil(19,000,000/3) = 25,333,336 B > 25,000,000 limit → share a link",
        "lesson": (
            "DCO-3707: a patron's resume portfolio is 19 MB, the mail service says attachments up to 25 MB, and sending still "
            "fails. Email was designed to carry text, so attachments are converted into text with an encoding called base64 "
            "before they travel. Base64 turns every three bytes into four characters, so the encoded file is about a third "
            "larger: four times the byte count divided by three, rounded up to a whole group. Nineteen million bytes become "
            "25,333,336 bytes, just over the 25,000,000-byte limit, which is why the message bounces even though the file "
            "looked small enough. An 18 MB file would encode to 24,000,000 bytes and squeak through. When something will not "
            "fit, do not split it into a dozen emails or squeeze the quality until the pictures blur. Upload it to a storage "
            "service, share a link with view-only permission, and mention in the message what the link is and how long it "
            "will stay up. Never attach other people's personal documents to practice messages; the lab uses only made-up "
            "byte counts."
        ),
        "assignment": "Submit lab_dco_attachment_fit JSON for DCO-3707: file and limit bytes, encoded size, fits, and plan.",
        "quiz": [
            ("Why do attachments grow before sending?", ["They are base64-encoded into text", "Mail servers add photos", "Files double in size", "The subject line is added"], "encoding"),
            ("Base64 turns every three bytes into how many characters?", ["Four", "Three", "Six", "Eight"], "4/3"),
            ("Nineteen million bytes encode to about how many?", ["25,333,336", "19,000,000", "38,000,000", "21,000,000"], "4·ceil(n/3)"),
            ("An 18 MB file against a 25 MB limit: fits?", ["Yes, 24,000,000 encoded bytes", "No", "Only zipped", "Only on mobile"], "edge"),
            ("A file will not fit. Best plan?", ["Share a link with view-only permission", "Split it into many emails", "Blur the pictures heavily", "Give up"], "share link"),
            ("What belongs in practice messages?", ["Made-up content only", "A friend's passport scan", "Real bank statements", "Other patrons' resumes"], "privacy"),
        ],
    },
    {
        "title": "Backups — three copies, two kinds of storage, one away from home",
        "lab_id": "lab_dco_backup_321",
        "worked_example": "laptop SSD + home USB HDD + cloud folder (offsite) → 3 copies, 3 media, 1 offsite; restore tested → plan_ok",
        "lesson": (
            "DCO-3808 begins with tears: a laptop died and took two years of family photos with it. A simple rule, called "
            "3-2-1, prevents most of these stories. Keep three copies of anything you would miss, the original plus two "
            "backups. Store them on at least two different kinds of storage, so one failure type, such as a batch of bad "
            "drives, cannot take everything. Keep one copy somewhere else, away from the house, so a fire, flood, or theft "
            "leaves something behind. The library's example plan has the photos on the laptop's SSD, a copy on a USB hard "
            "drive at home, and a copy in a cloud folder; that is three copies, three kinds of storage, and one offsite. "
            "There is a fourth rule people forget: a backup you have never restored is a hope, not a plan. Once a month, pick "
            "a random file and open it from each backup. Two copies on the same USB stick are one copy with extra steps, "
            "and a sync folder that mirrors deletions instantly is convenient but is not a backup on its own."
        ),
        "assignment": "Submit lab_dco_backup_321 JSON for DCO-3808: copies with media and offsite flags, each rule, restore_tested, plan_ok.",
        "quiz": [
            ("What does the '1' in 3-2-1 require?", ["One copy kept offsite", "One password", "One computer", "One backup per year"], "offsite"),
            ("Why use two kinds of storage?", ["So one failure type cannot take every copy", "It is cheaper", "It is faster", "It is the law"], "media diversity"),
            ("Two copies on the same USB stick count as what?", ["Effectively one copy", "Two backups", "A 3-2-1 plan", "An offsite copy"], "single point"),
            ("What makes a backup plan more than a hope?", ["A restore you have actually tested", "A larger drive", "A longer password", "A newer laptop"], "restore test"),
            ("A sync folder deletes a file everywhere when you delete it locally. What is it on its own?", ["Convenient, but not a backup", "A perfect backup", "An offsite archive", "Illegal"], "sync ≠ backup"),
            ("How often does the library suggest a test restore?", ["About once a month", "Never", "Every ten years", "Only after a disaster"], "cadence"),
        ],
    },
    {
        "title": "Readable screens — measuring colour contrast",
        "lab_id": "lab_dco_contrast",
        "worked_example": "#767676 on #ffffff → 4.54:1 passes AA normal text; #777777 on #ffffff → 4.48:1 fails AA normal, passes AA large",
        "lesson": (
            "DCO-3909: the library's new event flyer uses pale grey text, and a patron with low vision cannot read it. "
            "Readability can be measured. The W3C's Web Content Accessibility Guidelines, WCAG 2.2, define a contrast ratio "
            "between text and background colours. Each colour's red, green, and blue values are converted to a relative "
            "luminance, a weighted brightness in which green counts most and blue least, and the ratio is the lighter "
            "luminance plus 0.05 divided by the darker luminance plus 0.05. Black on white is 21 to 1; identical colours are "
            "1 to 1. Normal-size text needs at least 4.5 to 1 for level AA, and large text needs 3 to 1. The grey #767676 on "
            "white measures about 4.54 and just passes. One step lighter, #777777, measures about 4.48 and fails for normal "
            "text, even though most eyes cannot tell the two apart, which is exactly why you measure rather than guess. Use "
            "a contrast checker before printing or posting, and remember contrast is one accessibility check among many, "
            "not the whole job."
        ),
        "assignment": "Submit lab_dco_contrast JSON for DCO-3909: two colour pairs with ratio, aa_normal, and aa_large.",
        "quiz": [
            ("What minimum contrast does WCAG AA require for normal text?", ["4.5 to 1", "3 to 1", "7 to 1", "1.5 to 1"], "AA"),
            ("#777777 on white measures about 4.48. Does it pass AA for normal text?", ["No", "Yes", "Only on phones", "Only in print"], "below 4.5"),
            ("What is the contrast of black on white?", ["21 to 1", "4.5 to 1", "100 to 1", "1 to 1"], "maximum"),
            ("Which colour channel counts most in relative luminance?", ["Green", "Red", "Blue", "All equally"], "weights"),
            ("Why measure instead of eyeballing #767676 versus #777777?", ["They look alike but fall on opposite sides of 4.5", "Eyes are always wrong", "Measuring is faster", "Only designers can see colour"], "precision"),
            ("What is true about contrast and accessibility?", ["Contrast is one check among many", "Contrast alone makes a page accessible", "Contrast only matters for print", "It only applies to images"], "scope"),
        ],
    },
    {
        "title": "Personal digital safety plan — the page you keep",
        "lab_id": "lab_dco_safety_plan",
        "worked_example": "password manager yes; MFA on email yes; laptop/USB/cloud backups with tested restore; report phishing to the library IT desk; no real passwords in the plan",
        "lesson": (
            "DCO-3A10 asks each learner to leave the Library Lab with one page they will actually use. It names a password "
            "manager, because unique secrets for every site are impossible to remember otherwise. It turns on multi-factor "
            "sign-in for the email account first, since email is where every other password reset arrives, so whoever "
            "controls it controls the rest. It lists the backup copies by media and location, passes the 3-2-1 rule, and "
            "records the date of the last test restore. It names a real person or desk to show strange messages to, such as "
            "the library's IT desk, so nobody has to judge a convincing scam alone at midnight. It records which colours "
            "and font sizes work for the reader's eyes. It never contains an actual password, PIN, or recovery code; those "
            "belong in the manager or on paper locked away, not on a page that might be photographed. Mentors check the plan "
            "against six or more passed labs and ask the learner to show one step live, such as opening a file from the "
            "cloud backup."
        ),
        "assignment": "Submit lab_dco_safety_plan JSON for DCO-3A10: labs_passed, manager, MFA, backup copies, restore test, phishing contact, no real passwords.",
        "quiz": [
            ("Why turn on multi-factor sign-in for email first?", ["Password resets for other accounts arrive there", "Email is the slowest account", "It is the cheapest", "Email never gets attacked"], "reset hub"),
            ("What must never appear in the safety plan?", ["An actual password or recovery code", "The name of the password manager", "Backup locations", "A help-desk contact"], "secrets"),
            ("Why name a person or desk for strange messages?", ["So nobody judges a convincing scam alone", "To blame them later", "For marketing", "It is optional decoration"], "support"),
            ("What should the backup section record besides locations?", ["The date of the last test restore", "Every file name", "The drive's colour", "The purchase price"], "evidence"),
            ("During review, what does a mentor ask the learner to do?", ["Show one step live, such as opening a backed-up file", "Recite the quiz", "Reveal a password", "Buy new hardware"], "demonstration"),
            ("Where do recovery codes belong?", ["In the password manager or locked away on paper", "On the fridge", "In the safety plan", "In a text message to a friend"], "storage"),
        ],
    },
]

MID = [
    ("You are in /home/ben/Music and type ../../ana/Pictures. Where are you?", ["/home/ana/Pictures", "/home/ben/ana/Pictures", "/ana/Pictures", "/home/ben/Music/ana/Pictures"], "two levels up"),
    ("A path starts with a slash. What kind of path is it on macOS?", ["Absolute", "Relative", "Hidden", "Broken"], "root"),
    ("Which name helps you find a budget file next spring?", ["budget-2026-11.xlsx", "Untitled(3).xlsx", "asdf.xlsx", "final-final.xlsx"], "naming"),
    ("A 1 TB drive shows roughly how many GiB?", ["About 931", "About 1,000", "About 1,024", "About 512"], "10^12 / 2^30"),
    ("Your phone says a video is 800 MB and the USB stick has 0.7 GiB free. Will it fit?", ["No; 800 MB is about 0.745 GiB", "Yes, easily", "Only if renamed", "Only on Windows"], "convert"),
    ("Which unit do drive boxes usually use?", ["Decimal gigabytes", "Binary gibibytes", "Kilobits", "Megapixels"], "marketing unit"),
    ("A website forces a new password every 30 days. What does NIST SP 800-63B suggest instead?", ["Change on evidence of compromise", "Change daily", "Never use passwords", "Reuse old ones"], "rotation"),
    ("Which choice gives the most bits?", ["Six random diceware words", "Ten random digits", "Your pet's name plus 1", "Eight random lowercase letters"], "77.5 bits"),
    ("A friend uses one strong password everywhere. What is the risk?", ["One breached site exposes all accounts", "None, it is strong", "It slows the computer", "It expires faster"], "reuse"),
    ("Which link actually belongs to harborbank.example?", ["https://login.harborbank.example/start", "https://harborbank.example.verify.example.net", "https://harborbank-example.net", "https://example.net/harborbank.example"], "right end"),
    ("A text says 'your parcel is held, pay 2 dollars' with a link. Safest move?", ["Check the courier's own site or app directly", "Pay quickly", "Reply STOP with your card", "Forward to everyone"], "out-of-band"),
    ("A shortened link hides its address. What can you do before opening?", ["Use a preview feature or ask the desk", "Open it on a work computer", "Assume it is fine", "Enter your password to check"], "preview"),
    ("=SUM(B2:B4) returns 300. You change B3 from 100 to 150. What does the cell show now?", ["350", "300", "450", "150"], "live formula"),
    ("Which formula gives B2 as a share of total B7?", ["=B2/B7", "=B7/B2", "=B2+B7", "=SUM(B2)"], "share"),
    ("Your typed total disagrees with the rows. Which number do you trust?", ["The formula over the rows", "The typed total", "Neither", "The larger one"], "single source"),
    ("You type 900 characters in 3 minutes with 6 errors. Net WPM?", ["58", "60", "54", "300"], "60 − 2"),
    ("Why is a 'word' fixed at five characters in typing tests?", ["So long and short words count fairly", "Because English words are five letters", "To make scores higher", "It is a typo"], "fairness"),
    ("A 12,000,000-byte file encodes to how many base64 bytes?", ["16,000,000", "12,000,000", "24,000,000", "13,000,000"], "4/3"),
    ("Your plan has the laptop and a cloud folder only. Which 3-2-1 rule fails?", ["Three copies", "Two media", "One offsite", "None"], "count"),
    ("#595959 on white is about 7:1. What does it pass?", ["AA for normal and large text", "Nothing", "Only large text", "Only print"], "≥4.5"),
]

FINAL = [
    ("A form asks you to upload 'C:\\Users\\Mia\\Desktop\\id.pdf' but you saved it in Downloads. What changed?", ["The folder part of the path", "The file type", "The drive size", "The password"], "location"),
    ("Why do support staff ask 'where are you standing?' when a relative path fails?", ["Relative paths start from the current folder", "Paths are random", "It is small talk", "Absolute paths never work"], "cwd"),
    ("A 2 TB external drive shows about 1.82 TB on a laptop. What explains it?", ["Decimal versus binary units", "A broken drive", "Hidden viruses", "The cable"], "units"),
    ("A photo folder is 9.5 GB and the free space shows 9 GiB. Fits?", ["Yes, 9.5 GB is about 8.85 GiB", "No", "Exactly equal", "Cannot tell"], "convert first"),
    ("Which password policy best follows current NIST guidance?", ["Long passphrases, checked against breached lists, changed on compromise", "Eight characters, changed monthly", "Must include a symbol and a capital only", "No passwords at all"], "800-63B"),
    ("Why can a short password with symbols be weaker than a long lowercase one?", ["Length adds more bits than symbols when chosen at random", "Symbols are ignored", "Lowercase is encrypted", "It cannot be"], "length"),
    ("A website offers 'remember me' on a shared library computer. Best choice?", ["Decline and sign out when finished", "Accept", "Accept and leave the tab open", "Write the password on the desk"], "shared device"),
    ("An email from 'support@harborbank.example.alerts-help.example.org' asks for your PIN. Who sent it?", ["Whoever owns example.org", "Harbor Bank", "The library", "Your email provider"], "domain"),
    ("A message pressures you to act within ten minutes. What does urgency usually signal?", ["A tactic to stop you checking", "A genuine emergency always", "A system update", "A refund"], "pressure"),
    ("You must share a 60 MB video with a teacher. Most reliable method?", ["Upload and share a view-only link", "Attach it to one email", "Split it into twelve emails", "Print it"], "size"),
    ("A sheet's total is typed as 1,000 while the rows add to 1,100. What should you fix?", ["Replace the typed total with =SUM over the rows", "Delete a row", "Change the rows to match", "Hide the total"], "formula"),
    ("Which formula finds the average of B2 through B9?", ["=AVERAGE(B2:B9)", "=SUM(B2:B9)", "=B2/B9", "=MAX(B2:B9)"], "AVERAGE"),
    ("Your accuracy is 90% at 60 WPM. What should practice focus on?", ["Slowing down to raise accuracy", "Going faster", "Ignoring errors", "Stopping practice"], "accuracy"),
    ("Which posture reduces strain while typing?", ["Square to the keyboard with level wrists", "Wrists bent upward", "Keyboard on your lap at an angle", "Leaning on one elbow"], "ergonomics"),
    ("A backup drive sits beside the laptop in the same bag. Which threat defeats both?", ["The bag being stolen", "A typo", "A slow network", "A power cut at the library"], "offsite"),
    ("You last tested a restore two years ago. What is the plan's status?", ["Unproven until you test again", "Perfect", "Illegal", "Offsite"], "restore"),
    ("Why does a cloud sync folder alone fail 3-2-1?", ["Deletions and damage sync to every copy", "Clouds are offline", "It uses too much space", "It is always private"], "sync"),
    ("A flyer uses white text on pale yellow. What should you do before printing?", ["Measure the contrast ratio", "Add more yellow", "Use a smaller font", "Nothing"], "measure"),
    ("Large text needs at least what contrast for WCAG AA?", ["3 to 1", "4.5 to 1", "7 to 1", "2 to 1"], "large"),
    ("Which is a real accessibility improvement besides contrast?", ["Readable font size and clear link text", "Blinking text", "Text inside images only", "Light grey on white"], "beyond contrast"),
    ("A volunteer asks you to email them your password 'to help'. What do you do?", ["Refuse and show the request to the desk", "Send it", "Send half of it", "Post it on paper"], "never share"),
    ("Where should multi-factor sign-in be turned on first?", ["The email account", "A game account", "A shopping wish list", "The library catalogue"], "priority"),
    ("Which item belongs in a personal safety plan?", ["Who to ask when a message looks strange", "Your bank PIN", "Your recovery codes", "A copy of your ID"], "contents"),
    ("What does the Library Lab course claim when you finish?", ["Practice-based digital confidence, not a certification", "A guaranteed job", "A government licence", "Cyber-security certification"], "boundary"),
]
