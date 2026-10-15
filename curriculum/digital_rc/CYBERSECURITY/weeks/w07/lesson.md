# Week 7: Incident clock — detect, contain, eradicate, recover, lessons

NIST SP 800-61 Rev. 3, published April 2025, supersedes Rev. 2 and integrates incident response with CSF 2.0 cybersecurity risk management. The historical Harbor lab still uses a simplified detect → contain → eradicate → recover → lessons ordering contract. That fixture rule is not a claim that Rev. 3 mandates one universal linear sequence. A real response can revisit decisions as evidence and operational risk change. Preserve evidence, define authority and verify recovery rather than treating a step list as a complete response plan.

The ISC2 CC outline effective September 1, 2026 names Domain 5 Security Operations and Incident Response. Older outline mappings are historical alignment only, not the current examination requirements. Backing up model weights as a continuity asset is a 2026 sentence: if the summarizer is part of ops, its model files are not 'just a download.'

Tabletop artifact: a one-page clock with actual minutes, not 'ASAP.' ASAP is not a time.

Legal hold is a word you can say: do not tidy logs because they are embarrassing. Harbor's clock is written in local minutes on a paper card taped to the display so a volunteer does not have to remember the order under adrenaline. The card is not a substitute for the lab; it is how humans fail less.

## Concept and scope

Incident response coordinates preparation, analysis, containment, eradication, recovery and learning under defined authority. Actions can destroy evidence or disrupt essential service. A response plan must explain who can authorize a change and when to stop.

## Guided practice

Use a fictional suspected account misuse event. Write an incident clock with observed timestamps and explicitly simulated actions. Propose scoped containment, evidence preservation, a recovery verification and rollback if the action harms a required service. Expected result: every action has an owner, permission and success criterion.

## Independent evidence

Introduce a case where the evidence does not support malicious activity. Explain how the disposition changes without concealing the original alert. Do not revoke an account or isolate a real device for this paper exercise.

## Versioned primary references

ISC2 CC current outline (effective September 1, 2026): https://www.isc2.org/certifications/cc/cc-certification-exam-outline . NIST SP 800-61 Rev. 3 publication and supersession record: https://csrc.nist.gov/pubs/sp/800/61/r3/final . Checked October 15, 2026. These references identify current source versions; assessment-validity and professional-readiness judgments remain separate.

## Worked example

steps == [detect, contain, eradicate, recover, lessons]. contain index < eradicate index.
