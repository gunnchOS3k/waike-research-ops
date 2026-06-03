# FINAL — WAIKE Curriculum Requirements Handoff

## Repo

- **Repo:** `gunnchOS3k/waike-research-ops`
- **Path:** `/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/waike-research-ops`
- **Branch:** `curriculum-syllabi-assignments-case-study-system`
- **Commit:** `3f236894e66456fa9433fd3cbe0e75bdeef55e00`

## PR (do not merge)

https://github.com/gunnchOS3k/waike-research-ops/compare/main...curriculum-syllabi-assignments-case-study-system

```bash
gh pr create --repo gunnchOS3k/waike-research-ops \
  --base main \
  --head curriculum-syllabi-assignments-case-study-system \
  --title "Build WAIKE curriculum syllabi, assignments, 7GC case studies, and group project system" \
  --body "## Summary
- 18 course tracks with syllabi, assignments, group projects, rubrics, gunnchAI3k tutor cards
- 35 flagship 7GC case studies (5 per campus)
- Not exam-heavy assessment model (max 5–10% quizzes)
- make e2e generates and validates all results/

## Human review
- Case-study claims use synthetic teaching fixture language
- No accreditation claims
- See results/curriculum_issues.md for follow-up GitHub issues"
```

## Courses (18)

digital_confidence, general_it, hardware_engineering, software_engineering, networking, cybersecurity, cloud_devops, ai_ml_data, edge_ai_embedded, wireless_dsp_6g, robotics_control, project_management_agile_lss, data_visualization_bi, communication_ethics_professional_dev, game_development_interactive_media, gunnchos_device_os_product_lab, ai_ran_digital_twin_research, reproducible_research

## Generated outputs

- `results/catalog/course_catalog.md` + `.json`
- `results/syllabi/<course_id>_syllabus.md` (×18)
- `results/assignment_packs/<course_id>_assignments.md` (×18)
- `results/group_project_packs/<course_id>_group_project.md` (×18)
- `results/case_study_packs/<site>_case_studies.md` (×7)
- `results/instructor_packets/` + `results/student_packets/` (×18)
- `results/validation/curriculum_validation_report.md`

## Validation

All validators **PASS** via `make validate-curriculum` and `make e2e`.

## Issues

Tracked in `results/curriculum_issues.md` (GitHub issue creation pending `gh auth`).

## Edmund — review first

1. `curriculum/catalog.yaml` + `curriculum/assessment_model.yaml`
2. `case_studies/7gc/gary/homework_portfolio_access_lab/case_brief.md` (disclaimer language)
3. `rubrics/master_rubric.yaml`
4. `results/validation/curriculum_validation_report.md`
5. Flagship courses: `wireless_dsp_6g`, `cybersecurity`, `gunnchos_device_os_product_lab`, `ai_ran_digital_twin_research`

## Rerun

```bash
cd waike-research-ops
make e2e
```

## Gaps

- Standards mapping stubs (not all 11 frameworks fully expanded)
- Deep per-assignment prose (YAML skeletons + weekly titles)
- Live repo-integration labs need issue-driven upgrades
- Community partner validation not performed

---

```
Repo | Syllabi | Assignments | Group Projects | 7GC Case Studies | Rubrics | Validation | PR | Safe for Edmund Review?
waike-research-ops | 18 PASS | 18×8 weeks PASS | 18 PASS | 35 (7 sites) PASS | 8 rubrics PASS | PASS | pushed — open PR | YES
```
