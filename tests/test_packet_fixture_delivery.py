"""Check the public CLI and export path; no physical or learner result inferred."""
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
LAB=ROOT/'curriculum/digital_rc/COMPUTER_NETWORKING/learner_exercises/packet_model'


def execute(*arguments):
    return subprocess.run([sys.executable, 'packet_fixture.py', *arguments], cwd=LAB, capture_output=True, text=True, timeout=10)


def test_actual_fixture_cli_varies_evidence_and_decisions():
    normal=execute();expired=execute('--ttl','1');different=execute('--destination','203.0.113.4')
    assert all(p.returncode==0 for p in (normal,expired,different))
    a,b,c=[json.loads(p.stdout) for p in (normal,expired,different)]
    assert a['parsed']['ttl']==4 and a['decision']['ttl']==3
    assert b['decision']=={'action':'drop','reason':'ttl_expired'}
    assert c['decision']['port']=='uplink'
    assert len({p['parsed']['source_sha256'] for p in (a,b,c)})==3
    assert all(p['physical_measurement'] is False and p['competency_demonstrated'] is False for p in (a,b,c))


def test_invalid_fixture_never_reports_success():
    for arguments in (('--ttl','256'),('--destination','not-an-address')):
        process=execute(*arguments)
        assert process.returncode==2
        assert not process.stdout and 'rejected' in process.stderr
