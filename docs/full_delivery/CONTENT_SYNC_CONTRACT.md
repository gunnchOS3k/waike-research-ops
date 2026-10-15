# Browser content synchronization contract

Canonical owner: waike-research-ops. Stable 18 track IDs and the GENERAL_IT shared package are preserved. This revision does not create an additional curriculum or gradebook.

For GENERAL_IT, `course.json` contains the authored lesson body and worked example. Each `weeks/wNN/lesson.md` is its reader rendering. Changes must update both together and pass the synchronization test. Legacy generators are historical producers, not permission to overwrite authored revisions. Student/instructor packets and signed offline packs require explicit regeneration and review before a release; their old counts or signatures do not attest to this revision.

`scripts/export_browser_curriculum.py` reads full weekly lessons and explicitly allowlists public quiz fields. It exports assignments, lab instructions, glossary, syllabus and rubrics, with per-file SHA-256 and a content digest. The platform's generated JSON is disposable delivery output. Run the exporter from a clean committed curriculum checkout and record its commit. Do not hand-edit the generated JSON. The runtime evaluator reads the same quiz version and canonical private keys on the server. It rejects mismatched quiz hashes.

Formative guest practice is stateless on the server. Optional browser records are version-bound engagement/practice/draft records, not official assessment or mastery. Existing authenticated Hub assessment, authorization, submission and feedback remain authoritative. Keys must never be placed in public client bundles.

Offline packages, native installation, physical labs, practical assessment and all-course educational acceptance remain distinct release gates. No new public release is authorized by this work.
