# WAIKE ↔ gunnchAI3k API Contract

## Shared artifacts (versioned YAML)

- `waike-research-ops/knowledge_maps/waike_skill_tree.yaml`
- `gunnchAI3k/knowledge/skill_tree.yaml` (mirror)
- `curriculum_index.example.yaml` / `waike_course_index.example.yaml`

## Bot reads (public only)

Skill tree, course index, standards index, repo index, prompt packs.

## Bot must not store in git

Student transcripts, grades, Discord DMs bulk export, API keys.

## Commands

`/waike path|lesson|lab`, `/explain`, `/quizme`, `/portfolio`, `/mentor`, `/instructor`, `/standards`, `/integrity`, `/privacy`
