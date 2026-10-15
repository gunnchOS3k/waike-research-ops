# Week 9: USB story — a timeline is an argument

Events: login t=90, usb_insert t=100, file_copy t=140, usb_unmount t=155. Ordered, that is a story: someone logged into the kiosk, plugged a stick, copied essay.docx, and left. Forensics is the ordered story plus hashes, not a TV montage.

You will not image a stranger's phone. You will not bypass a lock screen. The fixture is the only evidence set. Chain of custody in this class is: who touched the JSON, when, and a hash of the file.

Memory of the volunteer is not evidence. The timeline is.

Portfolio artifact: a one-page timeline with hashes and a 'what we cannot claim' section. Cannot claim: identity of the human, intent, or that ada's burst is related. If two stories compete — volunteer says the stick was already there, JSON says insert at t=100 — you write both and you do not pick a winner to look decisive.

## Concept and scope

A timeline organizes observations using documented clocks and timezones. Order can support a hypothesis without proving causation. Source integrity, missing events and clock uncertainty affect interpretation. Redaction should remove unnecessary identifying data without obscuring essential evidence.

## Guided practice

Run the timeline example with 12:00 UTC and 12:30 at UTC+01:00. Expected result: the second displayed clock time is earlier in UTC. A timestamp without a timezone is rejected. Record the conversion and explain why an apparent sequence can reverse after normalization.

## Independent evidence

Add four fictional events and test equal timestamps. Annotate what was observed, what was inferred and what remains unknown. Do not claim a chain of custody for files you have not actually collected and preserved under an authorized process.

## Worked example

kinds after sort: login, usb_insert, file_copy, usb_unmount. Copy sits between insert and unmount.
