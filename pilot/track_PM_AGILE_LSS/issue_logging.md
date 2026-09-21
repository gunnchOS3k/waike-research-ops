# Issue logging — PM_AGILE_LSS

## Template

```
date_utc:
session_id:
track_id: PM_AGILE_LSS
severity_code:  # never full name in shared export
severity: blocker|confusion|a11y|safety|content_gap|tooling
summary:
repro_steps:
severity_or_synthetic: synthetic|local|hardware
owner:
status: open|mitigated|closed
```

## Severity

- **S0** safety / consent breach → stop session
- **S1** lab validator broken → switch to backup exercise
- **S2** content gap → continue with disclosed gap
- **S3** polish
