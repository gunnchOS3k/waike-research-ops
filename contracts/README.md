# WAIKE ↔ gunnchAI learning contracts

Machine-readable surfaces for **AI-WAIKE-MASTERY-001**.

- Discovery: `curriculum/digital_rc/*/course.json` (filesystem scan — **no hardcoded nine course names**)
- Emit: `python3 scripts/emit_waike_mastery.py`
- Artifacts: `artifacts/mastery/` and `ingest/learning_contract/waike_gunnchai_learning_contract.v1.json`

Modes (permission separation):

| Mode | Instructor keys | Self-grade | Notes |
|------|-----------------|------------|-------|
| MASTERY_BENCHMARK | no | no | Isolated grading agent after submission |
| LEARNER_TUTOR | no | no | Socratic; no final-answer dump |
| EDUCATOR_COPILOT | yes | no | HITL grading; no auto-publish |

Honesty: `REAL_STUDENT` / `REAL_TEACHER` / `HUMAN_E6` / `ACCREDITED` stay false without evidence.
