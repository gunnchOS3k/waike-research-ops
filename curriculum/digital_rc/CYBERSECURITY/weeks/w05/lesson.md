# Week 5: Hardening the image — guest off, keys on, bot sudo off

The Harbor workstation image: guest_login false, ssh_password_auth false, unattended_upgrades true, open_ports {22,443}, world_writable_home false, ai_agent_sudo false. That last flag is the 2026 identity lesson bolted onto a baseline that would otherwise look like 2014 CIS.

We use NIST SP 800-53 family names (AC, IA, SI, AU) as labels. We do not claim a FedRAMP boundary. Hardening is a diff against a fixture JSON, not a scan of the school's real network.

Patch pipelines are availability and integrity. An image that never patches is a museum. An image that patches during public hours is week 9 of General IT — here it is a control.

World-writable homes are how essays become everyone else's essays. Mode 777 is not hospitality. The image also disables guest login because a 'guest' on a SOC-adjacent workstation is an unowned session. If a visitor needs a browser, they use the Civic Tech Desk kiosk — a different image, a different zone, a different promise.

## Worked example

All six baseline flags must match. Mutating ai_agent_sudo true fails the lab.
