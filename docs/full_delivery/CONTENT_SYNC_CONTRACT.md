# Browser content synchronization contract

Canonical owner: waike-research-ops. Stable 18 track IDs and the GENERAL_IT shared package are preserved. This revision does not create an additional curriculum or gradebook.

For GENERAL_IT, SOFTWARE_BUILDER, COMPUTER_NETWORKING and CYBERSECURITY, `course.json` contains the authored lesson body and worked example. Each `weeks/wNN/lesson.md` is its reader rendering. Changes must update both together and pass the synchronization test. Legacy generators are historical producers, not permission to overwrite authored revisions. Student/instructor packets and signed offline packs require explicit regeneration and review before a release; their old counts or signatures do not attest to this revision.

`scripts/export_browser_curriculum.py` reads full weekly lessons and explicitly allowlists public quiz fields. It exports assignments, lab instructions, glossary, syllabus, rubrics and explicitly public learner-exercise source files, with per-file SHA-256 and a content digest. The platform's generated JSON is disposable delivery output. Run the exporter from a clean committed curriculum checkout and record its commit. Do not hand-edit the generated JSON. The runtime evaluator reads the same quiz version and canonical private keys on the server. It rejects mismatched quiz hashes.

Formative guest practice is stateless on the server. Optional browser records are version-bound engagement/practice/draft records, not official assessment or mastery. Existing authenticated Hub assessment, authorization, submission and feedback remain authoritative. Keys must never be placed in public client bundles.

Offline packages, native installation, physical labs, practical assessment and all-course educational acceptance remain distinct release gates. No new public release is authorized by this work.

## Recovered interrupted corrections

Recovered the existing uncommitted twelve-file Networking week-1/TCP and AI/ML week-1/leakage corrections from the preserved `pr59-ci-depth-quality-closure` worktree at 63ba9f25. Applied cleanly to this continuation after inspecting the source diff. Historical worktree remains untouched. Corrects ambiguous MTU/segmentation claims and unsupported causal/F1 claims, with matching generator, reader, presentation and private quiz-key changes. No experimental research repositories were modified. These corrections are teaching changes, not evidence of learner validation.


## WFD-2 source-binding repair and audience delivery

The manifest for track `CYBER_SOC` selects `curriculum/digital_rc/CYBERSECURITY`, not the historical `CYBER_SOC` directory. The earlier expansion was authored in the latter and therefore absent from that track's projection. Commit `687c39d336bd924ee1f9797b3c1bec3712c674e6` transfers its ten expanded lesson bodies/worked examples and public triage model into the selected package. Existing canonical lesson, lab, quiz and assessment identifiers remain intact. The legacy directory is preserved as historical content and is not a second authoring target.

`curriculum/canonical_packages/SOURCE_BINDINGS.json` records the 18 approved mappings as a binding guard, not a duplicate curriculum. The exporter compares it with every manifest. A regression deliberately changes CYBER_SOC's manifest selection to the legacy directory and requires export failure. Canonical CYBERSECURITY reader renderings are also checked against course.json.

Digital Confidence and IT Support retain the single GENERAL_IT source. Digital Confidence's audience-specific ten-unit guide and separate independent rubric live in GENERAL_IT/delivery/digital_confidence.json, version 2.0.0-review. The stateless grader lives in src/waike_course_ready/digital_confidence.py. Their combined SHA-256 binds a case, its browser projection and evaluation. The browser receives the learner guide, not the grader. Content updates invalidate case tokens and version-bound device drafts; tokens also expire after one hour. No historical frozen packet is overwritten.

The platform imports explicitly public guide/example files into newly generated TEST_ONLY packages. Native clients can read the included guide; these browser evaluator endpoints do not acquire offline execution support merely by inclusion. Offline/native installation and educational acceptance remain pending.
