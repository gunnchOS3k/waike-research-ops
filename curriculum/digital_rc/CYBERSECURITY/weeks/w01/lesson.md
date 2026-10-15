# Week 1: Harbor SOC — principles, governance, and the model that is also an asset

Harbor SOC is a classroom security operations center for WAIKE. Confidentiality, integrity, and availability still run the place. The ISC2 CC outline effective September 1, 2026 is the current study-alignment reference for this October 2026 edition. Its domains include Security Governance and Security Operations and Incident Response. This is WAIKE-authored instruction, not ISC2 exam content or certification.

Integrity for an AI helper means the training set and prompts are not a suggestion box for poisoning. If a bot summarizes tickets, a poisoned note can become a 'fact' in the next shift's head. Confidentiality means the model does not get raw patron essays. Availability means a model outage is a degraded SOC, not an excuse to skip containment.

Governance is GRC in small letters: who owns the kiosk image, who can approve sudo for a bot, what law or policy forbids storing library PANs. Transparency and bias are security-culture issues when a model triages which tickets look 'urgent.'

Security+ SY0-701 General Security Concepts (CIA, AAA, Zero Trust as words you can place) is the second alignment label. Still not an item harvest. Harbor's physical room is a spare office with two displays: one for the fixture SIEM, one for the ticket queue. Nobody 'hunts' on the public kiosk VLAN from a personal laptop. If the only screen is a phone, you export the JSON and read it like a log — you do not install random APK 'SOC tools' from a store screenshot.

## Concept and scope

A threat is a potential cause of harm; a vulnerability is a weakness; risk depends on context, likelihood and consequence. A control can reduce a risk without eliminating it. Security analysis begins by defining assets and authorized scope, including model files and the data used by an AI system.

## Guided practice

List fictional assets for Harbor SOC: redacted event records, analyst accounts, response runbooks and model configuration. For each, identify a confidentiality, integrity or availability concern and an owner. Expected result: every proposed control addresses a named concern instead of a vague instruction to make the system secure.

## Independent evidence

Choose a control, describe how to test it without sensitive information and state the residual risk. Mark the Harbor scenario as fictional; do not imply a deployed SOC or measured protection.

## Versioned primary references

ISC2 CC current outline (effective September 1, 2026): https://www.isc2.org/certifications/cc/cc-certification-exam-outline . NIST SP 800-61 Rev. 3 publication and supersession record: https://csrc.nist.gov/pubs/sp/800/61/r3/final . Checked October 15, 2026. These references identify current source versions; assessment-validity and professional-readiness judgments remain separate.

## Worked example

A triage bot with sudo would violate least privilege for a non-human identity and would turn a prompt injection into root. Harbor policy: bots read, humans close.
