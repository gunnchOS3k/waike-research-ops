#!/usr/bin/env python3
"""Evidence inventory; never infers educational acceptance from file counts."""
import json
from pathlib import Path
from export_browser_curriculum import build

ROOT=Path(__file__).resolve().parents[1]
bundle=build()
expanded={'GENERAL_IT','SOFTWARE_BUILDER','COMPUTER_NETWORKING','CYBER_SOC'}
rows=[]
for track in bundle['tracks']:
    lessons=[]
    for unit,lesson in enumerate(track['lessons'],1):
        lessons.append(dict(unit=unit,id=lesson['id'],source=lesson['path'],sha256=lesson['sha256'],
            authoring='PARTIALLY_AUTHORED',renderable=True,interactive=True,assessed=False,
            learner_acceptance_pending=True,expanded_this_continuation=track['packId'] in expanded,
            note='Technical and pedagogical acceptance not established; quiz evaluation is formative.'))
    rows.append(dict(trackId=track['trackId'],title=track['title'],package=track['packId'],
        full_reader_lessons=len(lessons),quizzes=len(track['quizzes']),assignments=len(track['assignments']),
        linked_lab_ids=sorted({l['labId'] for l in track['lessons']}),public_exercise_files=len(track['resources']),
        course_complete=False,lessons=lessons))
report=dict(schema='waike.full_delivery.evidence.v1',sourceCommit=bundle['sourceCommit'],overall='INCOMPLETE',courses=rows,
    meanings={'PARTIALLY_AUTHORED':'Authored instruction exists; all minimum complete-course gates have not been verified.',
              'RENDERABLE':'Full weekly Markdown is in the browser projection.',
              'INTERACTIVE':'Responses accepted and server-evaluated by formative practice; not a final practical.',
              'ASSESSED':'False: no authentic learner evaluation asserted.',
              'LEARNER_ACCEPTANCE_PENDING':'True for every course.'})
folder=ROOT/'docs/full_delivery'
(folder/'COURSE_EVIDENCE.json').write_text(json.dumps(report,indent=2)+'\n')
lines=['# WAIKE 18-course completeness matrix','', '**Overall: INCOMPLETE.** No course is marked complete. Source at inventory: `'+bundle['sourceCommit']+'`.', '',
       'All 180 lessons are PARTIALLY_AUTHORED review candidates, RENDERABLE and linked to INTERACTIVE formative quizzes; all are unASSESSED as authentic learner outcomes and LEARNER_ACCEPTANCE_PENDING. Forty weekly lessons in four shared packages were expanded with specific guided and independent practice in this continuation. The two General IT tracks share one ten-unit source; they are not two independently authored courses.', '',
       'Missing/outline-only files were not found in the exported weekly sequence. This does not establish complete depth, accurate prerequisites, meaningful practical assessment or readiness. See COURSE_EVIDENCE.json for every lesson ID, path, hash and separate flags.', '',
       '| Track | Full lesson reader | Quiz practice | Assignments | Distinct weekly labs | Download files | Remaining course gate |','|---|---:|---:|---:|---:|---:|---|']
for row in rows:
    gap='Expanded; full practical, assessment and educational review pending' if row['package'] in expanded else 'Full substantive review and practical development remain'
    lines.append(f"| {row['trackId']} | {row['full_reader_lessons']} | {row['quizzes']} | {row['assignments']} | {len(row['linked_lab_ids'])} | {row['public_exercise_files']} | {gap} |")
lines+=['','Counts are delivery evidence only. ASSESSED is false even where software tests pass: software verification is not evaluation of a learner. No occupation, credential or completion claim follows. The catalog examination cap was not changed.', '',
        '## Next dependency order','',
        'Finish General IT artifact schemas and verify independent submissions against the existing local lab runner; add graded assignment criteria to the authorized Hub. Complete Software Builder first-programming preparation, then verify the existing ForgeDesk practicals. Complete Networking and Cyber canonical lab contracts and reviewed practicals. Continue the remaining packages in taxonomy order, preserving the advanced and research tracks. Do not replace these steps with card counts or generated filler.', '',
        '## Known specific gaps','',
        '- GENERAL_IT: ten lessons expanded; full archive restore, account, service, ticket and change evidence still need learner execution and review. Historical packets/offline bundles must be regenerated before release.',
        '- SOFTWARE_BUILDER: a six-test downloadable example and ten expanded lessons; an actual first-programming prerequisite path and full infrastructure practicals remain distinct requirements.',
        '- NETWORKING_INFRA: ten expanded lessons and seven-test local model; canonical /32 host counting and malformed/empty evidence rejection are corrected and regression-tested. Packet parsing and physical-network validation are separate.',
        '- CYBER_SOC: ten expanded lessons and seven-test local model; actual protected evidence intake, case assessment and authorized operations remain required.',
        '- Other tracks: authored weekly files are readable and quiz practice runs; every minimum-course standard still requires substantive inspection. No blanket FULLY_AUTHORED flag is asserted.',
        '- All tracks: final assessment validity, human educational acceptance, learner pilots, accessibility beyond automated checks, and owner release approval remain open.', '']
(folder/'WAIKE_18_COURSE_COMPLETENESS_MATRIX.md').write_text('\n'.join(lines))
