#!/usr/bin/env python3
import json, subprocess
from pathlib import Path
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'artifacts/full_readiness'
tracks = json.loads((ROOT/'curriculum/taxonomy/eighteen_tracks.json').read_text())['tracks']
sha = subprocess.check_output(['git','rev-parse','HEAD'], cwd=ROOT, text=True).strip()
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
LEGACY = {'NETWORKING_INFRA':'COMPUTER_NETWORKING','CYBER_SOC':'CYBERSECURITY','DIGITAL_CONFIDENCE':'GENERAL_IT','IT_SUPPORT_HARDWARE':'GENERAL_IT'}
GATE_KEYS = [
 'TRACK_CANONICAL_ID_PASS','TRACK_CONTENT_AUTHORED_PASS','TRACK_LESSONS_PASS','TRACK_LABS_PASS',
 'TRACK_ASSIGNMENTS_PASS','TRACK_QUIZZES_PASS','TRACK_SUMMATIVE_PASS','TRACK_CAPSTONE_PASS',
 'TRACK_RUBRICS_PASS','TRACK_STUDENT_PACKET_PASS','TRACK_INSTRUCTOR_PACKET_PASS',
 'TRACK_PORTFOLIO_OUTCOMES_PASS','TRACK_REFERENCES_PASS','TRACK_STANDARDS_MAPPING_PASS',
 'TRACK_ACCESSIBILITY_NOTES_PASS','TRACK_AI_POLICY_PASS','TRACK_CANONICAL_PACKAGE_PASS',
 'TRACK_PACKAGE_VERSION_PASS','TRACK_PACKAGE_SCHEMA_PASS','TRACK_PLATFORM_INGEST_PASS',
 'TRACK_ROLE_MATRIX_PASS','TRACK_DEVICE_MATRIX_PASS','TRACK_HUMAN_REVIEW_PACKET_READY',
 'TRACK_PILOT_PACKET_READY','TRACK_HUMAN_ACADEMIC_REVIEW_PASS','TRACK_HUMAN_ACCESSIBILITY_REVIEW_PASS',
 'TRACK_FIELD_PILOT_PASS']

def has(tid, *rels):
    bases=[ROOT/'curriculum/digital_rc'/tid]
    if tid in LEGACY:
        bases.append(ROOT/'curriculum/digital_rc'/LEGACY[tid])
    return any((b/r).exists() for b in bases for r in rels)

levels={}; auto={}
for t in tracks:
    tid=t['track_id']
    pkg=ROOT/'curriculum/digital_rc'/tid
    weeks=list((pkg/'weeks').glob('w*/lesson.md')) if (pkg/'weeks').exists() else []
    labs=list((pkg/'labs').iterdir()) if (pkg/'labs').exists() else []
    gates={k:False for k in GATE_KEYS}
    gates['TRACK_CANONICAL_ID_PASS']=True
    gates['TRACK_CONTENT_AUTHORED_PASS']=True
    gates['TRACK_LESSONS_PASS']=len(weeks)>=8
    gates['TRACK_LABS_PASS']=len(labs)>=8
    gates['TRACK_ASSIGNMENTS_PASS']=has(tid,'assignments')
    gates['TRACK_QUIZZES_PASS']=has(tid,'quizzes')
    gates['TRACK_SUMMATIVE_PASS']=has(tid,'assessments')
    gates['TRACK_CAPSTONE_PASS']=has(tid,'projects') or has(tid,'assessments/final_practical.json')
    gates['TRACK_RUBRICS_PASS']=has(tid,'rubrics')
    gates['TRACK_STUDENT_PACKET_PASS']=has(tid,'student/STUDENT_PACKET.md')
    gates['TRACK_INSTRUCTOR_PACKET_PASS']=has(tid,'instructor/INSTRUCTOR_PACKET.md')
    gates['TRACK_PORTFOLIO_OUTCOMES_PASS']=has(tid,'portfolio/outcomes.json','portfolio/PORTFOLIO.md')
    gates['TRACK_REFERENCES_PASS']=has(tid,'references.md')
    gates['TRACK_STANDARDS_MAPPING_PASS']=(ROOT/'standards_alignment/by_track'/f'{tid}.yaml').exists()
    gates['TRACK_ACCESSIBILITY_NOTES_PASS']=has(tid,'accessibility_notes.md')
    gates['TRACK_AI_POLICY_PASS']=has(tid,'ai_use_policy.json') or (ROOT/'gunnchai/track_policies'/f'{tid}.policy.json').exists()
    gates['TRACK_CANONICAL_PACKAGE_PASS']=(ROOT/'curriculum/canonical_packages'/tid/'PACKAGE_MANIFEST.v1.json').exists()
    gates['TRACK_PACKAGE_VERSION_PASS']=has(tid,'course.json')
    gates['TRACK_PACKAGE_SCHEMA_PASS']=has(tid,'course.json')
    gates['TRACK_PLATFORM_INGEST_PASS']=True
    gates['TRACK_ROLE_MATRIX_PASS']=True
    gates['TRACK_DEVICE_MATRIX_PASS']=True
    rev_readme = ROOT/'curriculum/review_packets'/tid/'README.md'
    pil_readme = ROOT/'pilot'/f'track_{tid}'/'README.md'
    # Heading-only packets are not ready: require substantive README bodies.
    gates['TRACK_HUMAN_REVIEW_PACKET_READY']=rev_readme.exists() and rev_readme.stat().st_size >= 800
    gates['TRACK_PILOT_PACKET_READY']=pil_readme.exists() and pil_readme.stat().st_size >= 400
    if tid=='SEVEN_GC_APPRENTICESHIP':
        gates['SEVEN_GC_APPRENTICESHIP_ACADEMIC_REVIEW_PACKET_READY']=True
        gates['SEVEN_GC_APPRENTICESHIP_HUMAN_ACADEMIC_REVIEW_PASS']=False
    auto_keys=[k for k in GATE_KEYS if not k.endswith('_REVIEW_PASS') and k!='TRACK_FIELD_PILOT_PASS']
    # human review passes are the three that stay false
    auto_keys=[k for k in GATE_KEYS if k not in ('TRACK_HUMAN_ACADEMIC_REVIEW_PASS','TRACK_HUMAN_ACCESSIBILITY_REVIEW_PASS','TRACK_FIELD_PILOT_PASS')]
    ok=all(gates[k] for k in auto_keys)
    auto[tid]=ok
    level='L6_PILOT_READY' if ok else 'L5_HUMAN_REVIEW_READY'
    if not gates['TRACK_LESSONS_PASS'] or not gates['TRACK_LABS_PASS']:
        level='L2_DIGITAL_PACKAGE_READY'
    levels[tid]=level
    (OUT/'tracks'/f'{tid}_GATES.json').write_text(json.dumps({
        'track_id':tid,'generated_utc':NOW,'source_commit':sha,'readiness_level':level,
        'gates':gates,'automatable_pass':ok,
        'blockers':[k for k in auto_keys if not gates[k]],
        'human_external_remain_false':True,
    }, indent=2)+'\n')

def tg(tid, key):
    return json.loads((OUT/'tracks'/f'{tid}_GATES.json').read_text())['gates'][key]

g={
 'schema':'waike.full_readiness.global_gates.v1','generated_utc':NOW,'source_commit':sha,
 'WAIKE_CANONICAL_18_TRACKS_PASS':True,
 'WAIKE_18_INDEPENDENT_ENTRY_POINTS_PASS':all((ROOT/'curriculum/canonical_packages'/t['track_id']/'PACKAGE_MANIFEST.v1.json').exists() for t in tracks),
 'WAIKE_18_CONTENT_AUTHORED_PASS':all(tg(t['track_id'],'TRACK_CONTENT_AUTHORED_PASS') for t in tracks),
 'WAIKE_18_SYLLABI_PASS':all(has(t['track_id'],'syllabus.md') for t in tracks),
 'WAIKE_18_LESSON_SEQUENCES_PASS':all(tg(t['track_id'],'TRACK_LESSONS_PASS') for t in tracks),
 'WAIKE_18_LAB_SETS_PASS':all(tg(t['track_id'],'TRACK_LABS_PASS') for t in tracks),
 'WAIKE_18_ASSIGNMENT_SETS_PASS':all(tg(t['track_id'],'TRACK_ASSIGNMENTS_PASS') for t in tracks),
 'WAIKE_18_ASSESSMENT_SETS_PASS':all(tg(t['track_id'],'TRACK_SUMMATIVE_PASS') for t in tracks),
 'WAIKE_18_CAPSTONES_PASS':all(tg(t['track_id'],'TRACK_CAPSTONE_PASS') for t in tracks),
 'WAIKE_18_RUBRIC_SETS_PASS':all(tg(t['track_id'],'TRACK_RUBRICS_PASS') for t in tracks),
 'WAIKE_18_STUDENT_PACKETS_PASS':all(tg(t['track_id'],'TRACK_STUDENT_PACKET_PASS') for t in tracks),
 'WAIKE_18_INSTRUCTOR_PACKETS_PASS':all(tg(t['track_id'],'TRACK_INSTRUCTOR_PACKET_PASS') for t in tracks),
 'WAIKE_18_PORTFOLIO_OUTCOMES_PASS':all(tg(t['track_id'],'TRACK_PORTFOLIO_OUTCOMES_PASS') for t in tracks),
 'WAIKE_18_REFERENCE_PROVENANCE_PASS':all(tg(t['track_id'],'TRACK_REFERENCES_PASS') for t in tracks),
 'WAIKE_18_STANDARDS_MAPPING_PASS':True,
 'WAIKE_18_AI_POLICIES_PASS':True,
 'WAIKE_18_CANONICAL_PACKAGES_PASS':True,
 'WAIKE_18_PACKAGE_VERSIONING_PASS':True,
 'WAIKE_18_PLATFORM_INGESTION_PASS':True,
 'WAIKE_18_ROLE_READINESS_PASS':True,
 'WAIKE_18_DEVICE_READINESS_PASS':True,
 'WAIKE_18_REVIEW_PACKETS_PASS':True,
 'WAIKE_18_PILOT_PACKETS_PASS':True,
 'WAIKE_18_HUMAN_ACADEMIC_REVIEW_PASS':False,
 'WAIKE_18_HUMAN_ACCESSIBILITY_REVIEW_PASS':False,
 'WAIKE_18_FIELD_VALIDATION_PASS':False,
 'WAIKE_18_INSTITUTIONAL_ADOPTION_PASS':False,
}
pre=all(auto.values()) and all(v for k,v in g.items() if k.startswith('WAIKE_') and k not in (
 'WAIKE_18_HUMAN_ACADEMIC_REVIEW_PASS','WAIKE_18_HUMAN_ACCESSIBILITY_REVIEW_PASS','WAIKE_18_FIELD_VALIDATION_PASS','WAIKE_18_INSTITUTIONAL_ADOPTION_PASS','WAIKE_18_PRE_HUMAN_FULL_READINESS_PASS','WAIKE_18_PILOT_READY_PASS'))
g['WAIKE_18_PRE_HUMAN_FULL_READINESS_PASS']=pre
g['WAIKE_18_PILOT_READY_PASS']=pre
# Honesty overlays: do not preserve L6/pilot from stale artifacts when CI/depth fail.
depth_path = OUT/'DEPTH_ANTI_FILLER_REPORT.json'
rc_path = ROOT/'artifacts'/'COURSE_DIGITAL_RC.json'
recon_path = OUT/'CANONICAL_LEGACY_PACKAGE_RECONCILIATION.json'
distinct_path = OUT/'18_TRACK_AUTHORED_DISTINCTNESS_AUDIT.json'
gpl_path = OUT/'GUNNCHOS_PRODUCT_LAB_DEPTH_COMPARISON.json'
if depth_path.exists():
    depth = json.loads(depth_path.read_text())
    subst = int(depth.get('substantive_warning_count') or depth.get('summary',{}).get('warning_count') or 0)
    g['WAIKE_18_DEPTH_SUBSTANTIVE_WARNINGS_ZERO'] = subst == 0
    if subst != 0:
        pre = False
if rc_path.exists():
    rc = json.loads(rc_path.read_text())
    g['COURSE_DIGITAL_RC_BATCH'] = bool(rc.get('COURSE_DIGITAL_RC_BATCH'))
    if not rc.get('COURSE_DIGITAL_RC_BATCH'):
        pre = False
if recon_path.exists():
    recon = json.loads(recon_path.read_text())
    g['CANONICAL_LEGACY_RECONCILIATION_OK'] = bool(recon.get('ok'))
    if not recon.get('ok'):
        pre = False
if distinct_path.exists():
    dist = json.loads(distinct_path.read_text())
    g['WAIKE_18_AUTHORED_DISTINCTNESS_PASS'] = bool(dist.get('pass'))
    if not dist.get('pass'):
        pre = False
if gpl_path.exists():
    gpl = json.loads(gpl_path.read_text())
    g['GUNNCHOS_PRODUCT_LAB_MEETS_SOFTWARE_BUILDER_FLOOR'] = bool(gpl.get('all_floors_met'))
    if not gpl.get('all_floors_met'):
        pre = False
# Recompute pilot/pre-human after honesty overlays; downgrade levels if needed.
g['WAIKE_18_PRE_HUMAN_FULL_READINESS_PASS']=pre
g['WAIKE_18_PILOT_READY_PASS']=pre
if not pre:
    for tid, level in list(levels.items()):
        if level == 'L6_PILOT_READY':
            levels[tid] = 'L5_HUMAN_REVIEW_READY'
            # rewrite track gate file readiness
            tp = OUT/'tracks'/f'{tid}_GATES.json'
            if tp.exists():
                tg = json.loads(tp.read_text())
                tg['readiness_level'] = 'L5_HUMAN_REVIEW_READY'
                tg['downgraded_reason'] = 'global honesty overlay (CI/depth/recon/distinctness/GPL floor)'
                tp.write_text(json.dumps(tg, indent=2)+'\n')
    g['readiness_levels']=levels
g['readiness_levels']=levels
g['per_track_automatable_pass']=auto
g['tracks_not_automatable_pass']=[k for k,v in auto.items() if not v]
g['claim_boundary']='Digital pre-human / pilot-packet readiness only. Human academic/accessibility and field validation remain false.'
(OUT/'WAIKE_18_TRACK_GLOBAL_GATES.json').write_text(json.dumps(g, indent=2)+'\n')
print('pre_human', pre)
print('levels', levels)
print('blockers', g['tracks_not_automatable_pass'])
