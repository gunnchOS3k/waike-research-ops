# Traceability matrix — waike-research-ops

| Diagram element | Source path |
|---|---|
| Catalog 18 | `curriculum/catalog.yaml` |
| Digital-RC 14 | `curriculum/digital_rc/*/course.json` |
| Course package schema | `schema/waike_course_package.v1.json` |
| Pathway schema | `schema/waike_pathway.v1.json` |
| Completion schema | `schema/waike_completion_tracking.v1.json` |
| Pathway builder | `src/waike_ops/pathways.py` |
| Prerequisites | `src/waike_ops/prereqs.py` → `prerequisites.json` |
| Labs | `src/waike_course_ready/labs.py` |
| Learner/teacher ingest | `src/waike_course_ready/ingest.py` |
| Skill tree | `knowledge_maps/waike_skill_tree.yaml` |
| Instructor onboarding | `instructor_training/instructor_onboarding_path.md` |
| Learner journey test | `tests/journeys/test_learner_journey.py` |
| Instructor journey test | `tests/journeys/test_instructor_journey.py` |
| CI | `.github/workflows/ci.yml` |
| gunnchAI contract | `docs/17_WAIKE_TO_GUNNCHAI3K_API_CONTRACT.md` |
| 6G supporting-workload note | `docs/research/6G_WORKLOAD_RELEVANCE.md` |
