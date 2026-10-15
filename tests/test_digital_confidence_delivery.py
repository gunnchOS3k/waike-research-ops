import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from waike_course_ready.digital_confidence import parameters,evaluate

def valid(unit,p):
    f=lambda n:{'name':n,'text':p['text']}
    free=(p['size']-p['used']-p['reserved'])/p['size']*100
    return {1:{'file':f(p['filename'])},2:{'extension':'txt','action':'copy'},3:{'kiosk_admin':'no','operator_group':'helpdesk'},4:{'file':f(p['restored_filename'])},5:{'idle_seconds':p['idle_minutes']*60,'ticket_note':'credential reset requested','observation':'document empty after timeout'},6:{'free_percent':free,'policy':'meets' if free>=15 else 'below'},7:{'printer_address':p['printer_address'],'missing_name':'no record in this fixture','next_test':'check authorized local connection'},8:{'printing':'running','tracker':'stopped','verify_task':'print a fictional test page with permission'},9:{'window':'inside' if p['window_start']<=p['planned']<=p['window_end'] else 'outside','steps':'capture, apply, verify','recovery':'restore the recorded prior state and verify'},10:{'review_status':'pending instructor review','handoff':'method, evidence, limits and next action'},11:{'free_percent':free,'policy':'meets' if free>=15 else 'below','renamed':f(p['filename']),'restored':f(p['restored_filename']),'reflection':'I reopened the fictional note, changed a working copy and restored from a preserved copy. Byte equality does not prove independent performance.','next_action':'preserve files and request an authorized maintenance plan'}}[unit]

@pytest.mark.parametrize('seed',[0,1,3,4,99])
@pytest.mark.parametrize('unit',range(1,12))
def test_changed_case_positive_and_empty_negative(seed,unit):
    p=parameters(seed,unit);a=valid(unit,p);result=evaluate(unit,p,a)
    assert result['checks_passed'];assert result['competency_demonstrated'] is False
    assert not evaluate(unit,p,{})['checks_passed']

@pytest.mark.parametrize('value',['NaN','Infinity',True,{},[],None,''])
def test_invalid_numeric(value):
    p=parameters(3,6);a=valid(6,p);a['free_percent']=value
    assert not evaluate(6,p,a)['checks_passed']

def test_wrong_bytes_and_unrelated_case():
    p=parameters(4,1);a=valid(1,p);a['file']['text']+='changed'
    assert not evaluate(1,p,a)['checks_passed']
    assert not evaluate(1,parameters(5,1),valid(1,p))['checks_passed']

def test_replay_of_practice_is_not_independent_case():
    p=parameters(4,11);a=valid(11,p);a['renamed']=valid(1,parameters(3,1))['file']
    assert not evaluate(11,p,a)['checks_passed']
