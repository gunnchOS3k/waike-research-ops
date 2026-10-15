"""Pure data evaluation for the Digital Confidence pathway; no code execution/IO.

Evidence establishes properties of submitted fictional artifacts. It cannot attest
identity, physical performance, independence or authentic educational effectiveness.
"""
from decimal import Decimal, InvalidOperation
import hashlib
import re

def parameters(seed: int, unit: int):
    code=f'DC-{seed:08X}'
    return {'code':code,'filename':f'{code.lower()}-note.txt','restored_filename':f'{code.lower()}-restored.txt',
            'text':f'Fictional WAIKE practice note\nCase {code}\nNo personal information.\n',
            'size':256,'used':180+(seed%5)*10,'reserved':12,'idle_minutes':15+seed%4*5,
            'printer_address':f'192.0.2.{20+seed%100}', 'window_start':1080,'window_end':1260,'planned':(1140 if seed%2 else 1300)}

def evaluate(unit: int, p: dict, answers: dict):
    checks=[]
    def check(name,ok,feedback):checks.append({'id':name,'ok':bool(ok),'feedback':feedback})
    def decimal(name):
        v=answers.get(name)
        if isinstance(v,bool) or not isinstance(v,(str,int,float)):return None
        try:
            n=Decimal(str(v));return n if n.is_finite() else None
        except InvalidOperation:return None
    def file(name,expected_name):
        value=answers.get(name)
        ok=isinstance(value,dict) and set(value)=={'name','text'} and value.get('name')==expected_name and value.get('text')==p['text']
        check(name,ok,'Select the actual case file, with the required filename and unchanged UTF-8 text. Recheck source versus working copy if it differs.')
        return hashlib.sha256(value['text'].encode()).hexdigest() if ok else None
    if unit in (1,4):file('file',p['filename'] if unit==1 else p['restored_filename'])
    elif unit==2:
        check('extension',isinstance(answers.get('extension'),str) and answers['extension'].strip().lower()=='txt','Read the actual filename extension; this case uses plain text.')
        check('copy',answers.get('action')=='copy','A copy creates independently editable data; a shortcut points to another location.')
    elif unit==3:
        check('visitor_privilege',answers.get('kiosk_admin')=='no','Use least privilege for a shared visitor account. No real account is changed here.')
        check('operator_role',answers.get('operator_group')=='helpdesk','Match the operator role to the helpdesk task without granting administration.')
    elif unit==5:
        check('time',decimal('idle_seconds')==p['idle_minutes']*60,'Multiply the issued minutes by 60; use this case, not the earlier example.')
        check('privacy',answers.get('ticket_note')=='credential reset requested','Record the request, never the secret.')
        check('observation',answers.get('observation')=='document empty after timeout','Separate an observed symptom from an unsupported cause.')
    elif unit in (6,11):
        expected=Decimal(p['size']-p['used']-p['reserved'])/Decimal(p['size'])*100
        value=decimal('free_percent')
        check('capacity',value is not None and abs(value-expected)<=Decimal('0.01'),'Subtract used and reserve once, divide by total capacity, then multiply by 100. All values use GiB.')
        check('policy',answers.get('policy')==('meets' if expected>=15 else 'below'),'Compare the calculated percentage with the configured 15% policy. A below-policy finding can be correct.')
        if unit==11:
            file('renamed',p['filename']);file('restored',p['restored_filename'])
            reflection=answers.get('reflection','')
            check('reflection_present',isinstance(reflection,str) and 80<=len(reflection.strip())<=2000,'Provide your original method, one observed failure/recovery and one limitation. Quality requires instructor review.')
            check('safe_next_action',answers.get('next_action')=='preserve files and request an authorized maintenance plan','Preserve original work and use an authorized plan; do not delete files merely to pass a threshold.')
    elif unit==7:
        check('lookup',answers.get('printer_address')==p['printer_address'],'Use the issued table; the model sends no DNS queries.')
        check('missing_name',answers.get('missing_name')=='no record in this fixture','The closed fixture does not define public DNS behavior.')
        check('diagnosis',answers.get('next_test')=='check authorized local connection','Test the next relevant layer with permission; avoid disclosing private names.')
    elif unit==8:
        check('printing',answers.get('printing')=='running','The fixture requires printing.')
        check('tracker',answers.get('tracker')=='stopped','The fixture prohibits the toy tracker.')
        check('task_check',answers.get('verify_task')=='print a fictional test page with permission','A process state alone does not verify the user task.')
    elif unit==9:
        check('window',answers.get('window')==('inside' if p['window_start']<=p['planned']<=p['window_end'] else 'outside'),'Use this case time and the stated maintenance window.')
        check('order',answers.get('steps')=='capture, apply, verify','Capture recoverable state before the change; then verify.')
        check('recovery',answers.get('recovery')=='restore the recorded prior state and verify','Retain failures and test recovery; do not hide the outcome.')
    elif unit==10:
        check('review_status',answers.get('review_status')=='pending instructor review','Unreviewed work is pending; practice is not independent competence.')
        check('handoff',answers.get('handoff')=='method, evidence, limits and next action','A useful handoff lets another person understand the method and its limits.')
    else:raise ValueError('Unknown unit')
    return {'checks':checks,'checks_passed':bool(checks) and all(c['ok'] for c in checks),'kind':'independent_rehearsal' if unit==11 else 'guided_practice','competency_demonstrated':False,'human_review':'pending','evidence_sha256':hashlib.sha256(__import__('json').dumps(answers,sort_keys=True,ensure_ascii=True).encode()).hexdigest()}
