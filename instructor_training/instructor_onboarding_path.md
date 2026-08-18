# Instructor onboarding path

Facilitation, grading, UDL, gunnchAI3k boundaries. This is ops guidance, not an accredited teaching credential.

## Start here (digital-RC example)

Use **SOFTWARE_BUILDER** as the executable walk. Do not collapse catalog (18) and digital-RC (14) counts.

1. Read [`docs/LIMITATIONS_AND_NON_CLAIMS.md`](../docs/LIMITATIONS_AND_NON_CLAIMS.md). No carrier 6G, no Oulu affiliation, no certification granted.
2. Open [`curriculum/digital_rc/SOFTWARE_BUILDER/instructor/INSTRUCTOR_PACKET.md`](../curriculum/digital_rc/SOFTWARE_BUILDER/instructor/INSTRUCTOR_PACKET.md).
3. Confirm keys live only in `instructor/answer_keys.json` (not in learner ingest).
4. Run an empty lab to see the fail: `PYTHONPATH=src python3 scripts/run_course_labs.py --lab lab_git_conflict --empty`.
5. Grade with a human in the loop (**HITL**). gunnchAI3k `EDUCATOR_COPILOT` may read keys; it must not publish grades without a human (`mayPublishGradesWithoutHuman=false`).
6. Never commit transcripts, named grades, emails, or other PII. Local ingest only: `tools/private_transcript_ingestion/`.

## Weekly rhythm

- Lesson + lab JSON in the course package
- Rubrics under `curriculum/digital_rc/<COURSE>/rubrics/`
- AI-use modes on the packet (EXPLAIN/HINT/… and AI_ALLOWED/RESTRICTED/DISCLOSED/NO_AI)

## gunnchAI3k

Curriculum stays in this repo. Tutor engine: [gunnchAI3k](https://github.com/gunnchOS3k/gunnchAI3k). See `docs/GUNNCHAI3K_TUTOR_INTEGRATION.md` and `instructor_training/gunnchai_policy_for_instructors.md`.
