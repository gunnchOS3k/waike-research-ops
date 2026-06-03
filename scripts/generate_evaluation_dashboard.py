#!/usr/bin/env python3
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from waike_curriculum.evaluation.mock_data import mock_cohort
from waike_curriculum.evaluation.report import render_markdown
import json
out=ROOT/'results/evaluation'
out.mkdir(parents=True,exist_ok=True)
(out/'evaluation_dashboard_data.json').write_text(json.dumps(mock_cohort(),indent=2))
(out/'evaluation_dashboard.md').write_text(render_markdown(mock_cohort()))
(out/'privacy_safe_metrics_report.md').write_text('# Privacy-safe metrics\nNo PII.\n')
print('Generated evaluation dashboard')
