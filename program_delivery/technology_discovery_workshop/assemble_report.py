"""Offline aggregate report from declared observations; no network, DB or automatic grades."""
import argparse,csv,json,re
from pathlib import Path
CRITERIA=('files','restore','privacy','capacity','explanation')
STATES={'not_observed','needs_revision','observed'}
def summarize(rows):
    seen=set();counts={k:{s:0 for s in sorted(STATES)} for k in CRITERIA};reviewed=0
    for row in rows:
        code=row.get('participant_code','')
        if not re.fullmatch(r'P[0-9]{2,4}',code) or code in seen:raise ValueError('Use unique anonymous participant codes such as P01')
        seen.add(code)
        if any(row.get(k) not in STATES for k in CRITERIA):raise ValueError('Unknown or missing observation state')
        if any(row[k]!='not_observed' for k in CRITERIA) and row.get('reviewer_attested')!='yes':raise ValueError('Recorded observations require explicit reviewer attestation')
        for k in CRITERIA:counts[k][row[k]]+=1
        reviewed+=all(row[k]=='observed' for k in CRITERIA)
    return {'schema':'waike.workshop.aggregate.v1','workshop':'WAIKE-TECH-DISCOVERY-01','version':'1.0.0-owner-review','participation_records_supplied':len(seen),'instructor_reported_all_criteria_observed':reviewed,'criteria':counts,'course_completion_awarded':False,'certification_awarded':False,'authentic_reviewer_verification':'not performed by this utility','learning_effectiveness':'not established','limitation':'Counts summarize input declarations; they do not prove attendance, identity, independence or learning gain.'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('csv',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    with a.csv.open(newline='') as f:report=summarize(list(csv.DictReader(f)))
    a.output.write_text(json.dumps(report,indent=2)+'\n')
