# Week 1: Harbor SOC — principles, governance, and the model that is also an asset

Harbor SOC is a classroom security operations center for WAIKE. Confidentiality, integrity, and availability still run the place. The 2026-09-01 ISC2 CC outline renames the second domain toward governance and threads AI through all five. We prefer that upcoming outline. We do not copy ISC2 items.

Integrity for an AI helper means the training set and prompts are not a suggestion box for poisoning. If a bot summarizes tickets, a poisoned note can become a 'fact' in the next shift's head. Confidentiality means the model does not get raw patron essays. Availability means a model outage is a degraded SOC, not an excuse to skip containment.

Governance is GRC in small letters: who owns the kiosk image, who can approve sudo for a bot, what law or policy forbids storing library PANs. Transparency and bias are security-culture issues when a model triages which tickets look 'urgent.'

Security+ SY0-701 General Security Concepts (CIA, AAA, Zero Trust as words you can place) is the second alignment label. Still not an item harvest. Harbor's physical room is a spare office with two displays: one for the fixture SIEM, one for the ticket queue. Nobody 'hunts' on the public kiosk VLAN from a personal laptop. If the only screen is a phone, you export the JSON and read it like a log — you do not install random APK 'SOC tools' from a store screenshot.

## Worked example

A triage bot with sudo would violate least privilege for a non-human identity and would turn a prompt injection into root. Harbor policy: bots read, humans close.
