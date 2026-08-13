# Week 3 presentation — Cloud-shaped edges and the kiosk that must not walk into the SOC

## Slide 1 — Cold open
matrix[(kiosk,soc)]=deny; [(soc,kiosk)]=allow_syslog_only; [(guest,staff)]=deny.

## Slide 2 — Teaching beat
Networking and cloud security on the upcoming CC outline is not a vendor catalog. Harbor uses three zones: kiosk, staff, soc. Kiosk to SOC is deny. SOC to kiosk is allow_syslog_only. Guest to staff is deny. Shared responsibility in cloud language means: if we used a SaaS ticketing tool, they patch the app, we still classify data.

## Slide 3 — Numbers on the board
Do the worked example live. Do not skip to the quiz.

## Speaker notes
If a learner asks for a certification dump, refuse and point at the alignment JSON. Keys stay instructor-only.
