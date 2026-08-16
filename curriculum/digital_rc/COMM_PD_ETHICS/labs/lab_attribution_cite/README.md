# lab_attribution_cite — attribution cite

PD-2511 citation discipline. reuse_class ∈ {PUBLIC_REFERENCE_ONLY, FAIR_USE_PARAPHRASE, ORIGINAL}. quote_chars ≤120. paraphrase ≥40 in WAIKE words. Verbatim dumps fail. Certs stay aligned-not-granted.

## Student artifact
Required keys: claim, source_title, reuse_class, quote_chars, paraphrase.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Cite ISC2 theme labels for PD-2511 without dumping chapters.
```
python3 scripts/run_course_labs.py --lab lab_attribution_cite --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_attribution_cite --empty
```

## Wrong submissions
FULL_COPY, quote_chars>120, or 'verbatim dump' paraphrase fail.
