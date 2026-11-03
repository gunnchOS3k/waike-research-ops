# Week 7: Attachments — why a 19 MB file will not fit under 25 MB

DCO-3707: a patron's resume portfolio is 19 MB, the mail service says attachments up to 25 MB, and sending still fails. Email was designed to carry text, so attachments are converted into text with an encoding called base64 before they travel. Base64 turns every three bytes into four characters, so the encoded file is about a third larger: four times the byte count divided by three, rounded up to a whole group. Nineteen million bytes become 25,333,336 bytes, just over the 25,000,000-byte limit, which is why the message bounces even though the file looked small enough. An 18 MB file would encode to 24,000,000 bytes and squeak through. When something will not fit, do not split it into a dozen emails or squeeze the quality until the pictures blur. Upload it to a storage service, share a link with view-only permission, and mention in the message what the link is and how long it will stay up. Never attach other people's personal documents to practice messages; the lab uses only made-up byte counts.

## Worked example

19,000,000 B → base64 4·ceil(19,000,000/3) = 25,333,336 B > 25,000,000 limit → share a link
