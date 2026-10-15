# Week 10: Harbor capstone — evidence locker design then operate

CS161's depth pattern is design-document checkpoint then implementation. Harbor's group project is an evidence locker policy: what is stored, who can read, how hashes work, how a bot may summarize without seeing PII. You will not implement Berkeley's file-share. You will implement a tiny policy checker in Python that refuses PII fields and bot-close.

Practical: run SIEM, hardening, IAM, segmentation, IR clock, toy parser, timeline. All must compute ok true. Negative fixtures must fail.

Career: NICE-aligned SOC analyst adjacent, ISC2 CC upcoming domains, Security+ operations. No certification is granted. No exam dump is included.

Scope paragraph: you still do not scan what you do not own. The capstone demo is the seven lab JSON files, the policy checker rejecting a password field, and a two-minute talk that names one thing Harbor cannot claim. Applause is not evidence.

## Concept and scope

A defensible SOC handoff connects an alert, evidence, hypothesis, authorized action, retest and unresolved uncertainty. Automated checks support particular conditions; they do not replace human judgment or authorize live action.

## Guided practice

Run the seven triage tests, then prepare a fictional case containing the rule match, access-policy checks, normalized timeline and containment proposal. Expected result: the report calls the alert an investigation candidate and keeps the proposed action separate from an executed action. Preserve unfavorable or ambiguous evidence.

## Independent evidence

Submit the redacted case, exact code version, test output and claim-to-evidence table. Include one reason the toy model cannot establish professional SOC readiness. Practical review and real learner acceptance remain pending until actual evidence meets the canonical criteria.

## Worked example

Policy checker rejects records with password= and rejects harbor-bot as closer. Seven labs ok, three negatives fail as required.
