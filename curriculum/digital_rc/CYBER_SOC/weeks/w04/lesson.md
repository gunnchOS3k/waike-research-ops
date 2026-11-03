# Week 4: Indicator hygiene — hash it, defang it, then compare

SOC-2404 arrives with a suspicious attachment name and a link from a user report. Indicators of compromise are only useful if you can compare them exactly and pass them around safely. For files that means a cryptographic hash: SHA-256 turns any sequence of bytes into a 64-character fingerprint, and a single changed byte produces an unrelated digest, so the lab recomputes the hash from the inert sample text instead of trusting a pasted value. For links it means defanging before the indicator goes into a ticket, chat, or report: write hxxp instead of http and bracket every dot in the host, so update-check.example.net becomes update-check[.]example[.]net and nobody's mail client turns it into a clickable trap. Only after both steps do you check the desk's indicator list. Here the sample hash and the domain are both on it, so the answer is a match and the ticket goes to the phishing playbook. A miss does not mean safe, it means unknown, and the course's sample is inert text, never real malware, so nobody downloads or detonates anything on a personal laptop.

## Worked example

sha256('WAIKE-SOC training sample: …') = fc6c0f88…e657; http://update-check.example.net/payload → hxxp://update-check[.]example[.]net/payload; on IOC list → match
