.PHONY: deepen-courses generate-lessons generate-labs generate-assignment-bodies \
	generate-group-project-depth generate-case-study-depth generate-industry-alignment \
	generate-deep-student-packets generate-deep-instructor-packets generate-portfolio-evidence-index \
	validate-depth generate-syllabi generate-assignments generate-group-projects generate-case-studies \
	generate-rubrics export-catalog validate-curriculum e2e map smoke

PY := PYTHONPATH=src

deepen-courses:
	$(PY) python3 scripts/deepen_all_courses.py

generate-lessons generate-labs generate-assignment-bodies generate-group-project-depth: deepen-courses

generate-case-study-depth: deepen-courses

generate-industry-alignment: deepen-courses

generate-deep-student-packets generate-deep-instructor-packets generate-portfolio-evidence-index: deepen-courses

validate-depth:
	python3 scripts/validate_depth_all.py

generate-syllabi:
	$(PY) python3 scripts/generate_syllabi.py --all

generate-assignments:
	$(PY) python3 scripts/generate_assignment_pack.py --all

generate-group-projects:
	$(PY) python3 scripts/generate_group_project_pack.py --all

generate-case-studies:
	$(PY) python3 scripts/generate_7gc_case_study_pack.py --all

generate-rubrics:
	python3 scripts/generate_rubric_tables.py

export-catalog:
	$(PY) python3 scripts/export_course_catalog.py
	$(PY) python3 scripts/export_instructor_packet.py --all
	$(PY) python3 scripts/export_student_packet.py --all

validate-curriculum:
	python3 scripts/validate_all_curriculum.py

map:
	python3 scripts/export_course_repo_map.py

e2e:
	@mkdir -p results/e2e results/validation results/catalog results/syllabi \
		results/assignment_packs results/group_project_packs results/case_study_packs \
		results/instructor_packets results/student_packets results/deep_course_packets \
		results/deep_student_packets results/deep_instructor_packets results/portfolio_evidence_index
	$(MAKE) generate-syllabi generate-assignments generate-group-projects generate-case-studies generate-rubrics export-catalog
	$(MAKE) deepen-courses
	$(MAKE) validate-curriculum validate-depth
	python3 scripts/export_course_repo_map.py 2>&1 | tee results/e2e/e2e_terminal_output.txt
	$(PY) python3 scripts/generate_all_campus_tracks.py >> results/e2e/e2e_terminal_output.txt
	$(PY) pytest -q >> results/e2e/e2e_terminal_output.txt
	python3 scripts/validate_waike_artifacts.py >> results/e2e/e2e_terminal_output.txt || true
	python3 scripts/run_all_tool_exports.py 2>> results/e2e/e2e_terminal_output.txt || true
	$(MAKE) e2e-tooling 2>> results/e2e/e2e_terminal_output.txt || true
	python3 scripts/e2e_check_required_artifacts.py

smoke: e2e

e2e-tooling:
	@mkdir -p results/tool_exports
	python3 scripts/run_all_tool_exports.py 2>/dev/null || python3 scripts/check_optional_backends.py || true

e2e-sionna e2e-deepmimo e2e-aerial e2e-oran:
	@echo "Optional target $@ — requires external install"
