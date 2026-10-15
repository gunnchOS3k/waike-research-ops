import importlib.util
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('browser_export',ROOT/'scripts/export_browser_curriculum.py')
module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)

def test_all_tracks_full_lessons_no_private_keys():
    bundle=module.build()
    assert len(bundle['tracks'])==18
    for track in bundle['tracks']:
        assert len(track['lessons'])==len(track['quizzes'])==len(track['assignments'])==10
        assert all('/weeks/' in l['path'] for l in track['lessons'])
        for lesson in track['lessons']:
            assert any(l['id']==lesson['labId'] for l in track['labs'])
        for quiz in track['quizzes']:
            assert quiz['items']
            assert all(set(i)<= {'id','kind','stem','choices'} for i in quiz['items'])
        assert not any('/instructor/' in x['path'] for key in ('lessons','quizzes','assignments','labs','references','portfolio') for x in track[key])
    assert '"answer_index"' not in json.dumps(bundle)

def test_general_it_lesson_rendering_matches_authoring_source():
    folder=ROOT/'curriculum/digital_rc/GENERAL_IT'
    course=json.loads((folder/'course.json').read_text())
    for w in course['weeks']:
        expected=f"# Week {w['week']}: {w['title']}\n\n{w['lesson']['body_md']}\n\n## Worked example\n\n{w['lesson']['worked_example']}\n"
        assert (folder/f"weeks/w{w['week']:02d}/lesson.md").read_text()==expected
        assert 'Expected result' in expected or 'Expected interpretation' in expected
