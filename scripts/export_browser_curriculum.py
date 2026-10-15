#!/usr/bin/env python3
"""Read-only, allowlisted browser projection of the canonical 18-track curriculum.

Never exports instructor directories, solutions, learner records or assessment keys.
Generated JSON is a delivery artifact, not another authoring source.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def build(root=ROOT):
    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    tracks = json.loads((root/'curriculum/taxonomy/eighteen_tracks.json').read_text())['tracks']
    output = []
    def item(path, item_id=None, title=None):
        text = path.read_text()
        return dict(id=item_id or path.stem, title=title or next((s.lstrip('# ') for s in text.splitlines() if s.startswith('# ')), path.stem),
                    path=path.relative_to(root).as_posix(), sha256=hashlib.sha256(text.encode()).hexdigest(), markdown=text)
    for t in tracks:
        manifest = json.loads((root/f"curriculum/canonical_packages/{t['track_id']}/PACKAGE_MANIFEST.v1.json").read_text())
        folder = root/'curriculum/digital_rc'/manifest['package_dir']
        course = json.loads((folder/'course.json').read_text())
        lessons, quizzes, assignments = [], [], []
        for w in course['weeks']:
            n = w['week']
            lesson = item(folder/f'weeks/w{n:02d}/lesson.md', w['lesson']['lesson_id'], w['title'])
            lesson['labId'] = w['lab_id']
            lessons.append(lesson)
            qpath = folder/f'quizzes/q{n:02d}.json'
            q = json.loads(qpath.read_text())
            public_items = [{k: v for k,v in i.items() if k in ('id','kind','stem','choices')} for i in q['items']]
            quiz = item(qpath, q['quiz_id'], f"Week {n} practice quiz")
            quiz['items'] = public_items
            quiz['markdown'] = '\n\n'.join(i['stem'] for i in public_items)
            quizzes.append(quiz)
            assignments.append(item(folder/f'assignments/a{n:02d}.md'))
        labs = [item(p, p.parent.name) for p in sorted((folder/'labs').glob('*/README.md'))]
        extras = [item(p) for p in [folder/'glossary.md', folder/'syllabus.md', folder/'rubrics/rubrics.json', folder/'references.md', folder/'prerequisites.json'] if p.is_file()]
        resources = [item(p) for p in sorted((folder/'learner_exercises').rglob('*')) if p.is_file() and p.suffix in ('.py','.md')]
        portfolio = [item(p) for p in sorted((folder/'portfolio').glob('*.md'))]
        digest = hashlib.sha256(json.dumps([x['sha256'] for x in lessons+quizzes+assignments+labs+extras+portfolio+resources]).encode()).hexdigest()
        delivery=None
        dpath=folder/'delivery/digital_confidence.json'
        if t['track_id']=='DIGITAL_CONFIDENCE' and dpath.is_file():
            code=(root/'src/waike_course_ready/digital_confidence.py').read_bytes()
            delivery=dict(definition=json.loads(dpath.read_text()), revision=hashlib.sha256(dpath.read_bytes()+code).hexdigest(), sourcePath=dpath.relative_to(root).as_posix())
            digest=hashlib.sha256((digest+delivery['revision']).encode()).hexdigest()
        output.append(dict(trackId=t['track_id'], title=t['title'], packId=manifest['package_dir'], contentRootSha256=digest,
                           sourceCommit=sha, offlinePackDeclared=False, delivery=delivery, lessons=lessons, quizzes=quizzes,
                           assignments=assignments, labs=labs, portfolio=portfolio, references=extras, resources=resources,
                           prerequisites=json.loads((folder/'prerequisites.json').read_text())))
    assert len(output)==18
    # Explicit field allowlist above; these sentinel checks guard accidental future expansion.
    encoded = json.dumps(output, ensure_ascii=False)
    assert '"answer_index"' not in encoded
    return dict(schema='waike.browser.curriculum.v2', owner='waike-research-ops', sourceCommit=sha, tracks=output)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args=parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), indent=2, ensure_ascii=False)+'\n')
