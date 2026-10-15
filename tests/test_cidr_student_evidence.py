"""Student-evidence regressions; no golden fixture is substituted for a submission."""
import ipaddress
import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from waike_course_ready.labs import lab_cidr_math

def case(cidr, usable):
    net=ipaddress.IPv4Network(cidr,strict=False)
    return {'cidr':cidr,'network':str(net.network_address),'broadcast':str(net.broadcast_address),'usable':usable}

@pytest.mark.parametrize('cidr,usable',[('192.0.2.70/26',62),('192.0.2.5/30',2),('192.0.2.0/31',2),('192.0.2.1/32',1)])
def test_correct_independently_supplied_arithmetic(cidr,usable):
    assert lab_cidr_math(submission={'cases':[case(cidr,usable)]}).ok

def test_zero_is_wrong_for_a_host_route():
    assert not lab_cidr_math(submission={'cases':[case('192.0.2.1/32',0)]}).ok

@pytest.mark.parametrize('cases',[[],None,{},'PASS',[{}],[{'cidr':'not-a-prefix'}],[case('192.0.2.1/32',True)]])
def test_missing_malformed_or_non_numeric_evidence_never_passes(cases):
    assert not lab_cidr_math(submission={'cases':cases}).ok
