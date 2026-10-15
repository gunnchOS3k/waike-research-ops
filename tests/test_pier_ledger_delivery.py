"""Exercise the downloaded CLI boundary, source evidence and failure behavior."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
LAB=ROOT/'curriculum/digital_rc/DATA_DASHBOARDS/learner_exercises/pier_ledger'


def run(*args):
    return subprocess.run([sys.executable, *map(str,args)], cwd=LAB, capture_output=True, text=True, timeout=10)


def test_actual_downloaded_program_produces_source_bound_evidence(tmp_path):
    source=tmp_path/'fictional.csv'; report=tmp_path/'evidence.json'
    assert run('case_data.py', source).returncode==0
    result=run('ledger.py', source, report)
    assert result.returncode==0, result.stderr
    evidence=json.loads(report.read_text())
    assert evidence['source_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
    assert evidence['mean_headcount']==50 and evidence['p95_nearest_rank']==80
    assert evidence['selected_rows']==[['v3',60],['v4',80]]
    assert evidence['competency_demonstrated'] is False
    assert evidence['instructor_review']=='pending'
    # The generator and analyzer both preserve existing evidence on retry.
    before_source=source.read_bytes(); before_report=report.read_bytes()
    assert run('case_data.py', source).returncode !=0
    assert source.read_bytes()==before_source
    assert run('ledger.py', source, report).returncode !=0
    assert report.read_bytes()==before_report


def test_changed_inputs_and_bad_inputs_are_not_manufactured_success(tmp_path):
    source=tmp_path/'independent.csv'; report=tmp_path/'case.json'
    assert run('case_data.py',source,'--seed','902').returncode==0
    assert run('ledger.py',source,report,'--threshold','60','--now','2026-10-01T20:00:00Z').returncode==0
    result=json.loads(report.read_text())
    assert result['rows_in']==12 and result['rows_out']==10
    assert result['freshness']['within_policy'] is False
    assert all(row[1]>60 for row in result['selected_rows'])
    report.unlink()
    source.write_text('PASS')
    bad=run('ledger.py',source,report)
    assert bad.returncode==2 and not report.exists()
    assert 'rejected' in bad.stderr
    source.write_bytes(b'x'*65537)
    assert run('ledger.py',source,report).returncode==2 and not report.exists()
