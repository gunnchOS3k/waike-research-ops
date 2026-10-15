# Week 6: Segmentation that survives a stolen laptop

A stolen staff laptop should not become a SOC pass. That's the point of zones and device posture. Harbor's matrix already denies guest→staff. Stolen-laptop story: revoke the identity (week 2), watch the logs (week 4), and do not widen the matrix 'temporarily.'

Microseg is a word. A usable version here: kiosk processes cannot open SMB to staff file shares. If you need a file, you use the desk procedure from General IT, not a hole in the firewall.

Cloud security concept: security groups are ACLs with opinions. We write the opinion in the matrix rather than clicking a console.

Tabletop: the fictional laptop is reported missing at 16:40. An authorized responder considers session revocation, device access restrictions and evidence preservation according to the incident plan. A recorded DHCP lease is evidence of an allocation, not proof of current physical presence. Lease expiry does not itself revoke identity or guarantee that a device cannot communicate. Do not claim a foreign SSID or ongoing traffic without corresponding observations.

## Concept and scope

Segmentation limits permitted communication paths according to a policy. Phishing defense includes identity, user reporting, message handling and response; neither a separate subnet nor a convincing visual appearance establishes message legitimacy.

## Guided practice

Draw fictional staff, guest and response zones. Specify permitted flows with purpose and direction. Then analyze a message requesting a password through an unfamiliar link. Expected result: preserve a redacted report and use an established reporting channel; do not enter a credential to test the link.

## Independent evidence

Write a denial test for guest access to the response zone and a process for reporting a suspected phish. Keep simulation separate from performed firewall or email-system changes. Do not send a deceptive message to real users as an unapproved exercise.

## Worked example

Revoke omar's sessions before rewriting the zone matrix. Matrix widen is not containment.
