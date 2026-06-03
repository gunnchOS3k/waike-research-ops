def test_learning_paths():
    from pathlib import Path
    import subprocess, sys
    subprocess.check_call([sys.executable, 'scripts/generate_industry_tooling_learning_paths.py'], cwd=Path(__file__).resolve().parents[1])
