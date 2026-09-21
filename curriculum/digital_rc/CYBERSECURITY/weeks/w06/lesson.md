# Week 6: Segmentation that survives a stolen laptop

A stolen staff laptop should not become a SOC pass. That's the point of zones and device posture. Harbor's matrix already denies guest→staff. Stolen-laptop story: revoke the identity (week 2), watch the logs (week 4), and do not widen the matrix 'temporarily.'

Microseg is a word. A usable version here: kiosk processes cannot open SMB to staff file shares. If you need a file, you use the desk procedure from General IT, not a hole in the firewall.

Cloud security concept: security groups are ACLs with opinions. We write the opinion in the matrix rather than clicking a console.

Tabletop: laptop gone at 16:12, reported 16:40. Containment is identity revoke and session kill, not a press release. At 16:41 you also mark the laptop's last DHCP lease as untrusted and watch whether it still talks. A stolen device that keeps renewing is still in the story until the lease dies or you see it on a foreign SSID.

## Worked example

Revoke omar's sessions before rewriting the zone matrix. Matrix widen is not containment.
