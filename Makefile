.PHONY: test demo demo-research benchmark-toy map

test:
	pytest -q

map:
	python3 scripts/export_course_repo_map.py
