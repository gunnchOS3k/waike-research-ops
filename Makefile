.PHONY: map e2e

map:
	python3 scripts/export_course_repo_map.py

e2e:
	@mkdir -p results/e2e
	python3 scripts/export_course_repo_map.py 2>&1 | tee results/e2e/e2e_terminal_output.txt
	python3 scripts/validate_waike_artifacts.py >> results/e2e/e2e_terminal_output.txt
	python3 scripts/e2e_check_required_artifacts.py
