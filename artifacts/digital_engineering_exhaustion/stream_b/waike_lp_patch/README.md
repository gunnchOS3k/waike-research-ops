# WAIKE Learning Platform patch (Stream B)

Apply onto `gunnchos-waike-learning-platform` @ `7ccb64459df088d41655af51c959a7bbbac849a3` (accepted main).

## Why a patch bundle?

This agent workspace can read the LP repo but cannot write its `.git` metadata (outside Cursor workspace roots). Files here are the engineering delta for an owner-applied **DRAFT** PR.

## Files

| Bundle file | Destination |
|-------------|-------------|
| `telemetry.py` | `services/hub/app/modules/telemetry.py` |
| `test_telemetry.py` | `tests/exhaustion/test_telemetry.py` |
| `main.py` | `services/hub/app/main.py` (adds TelemetryService wiring) |
| `routes_gate_c.py` | `services/hub/app/api/routes_gate_c.py` (adds `/telemetry/*`) |

## Verify

```bash
PYTHONPATH=services/hub python3 -m pytest -q tests/exhaustion/test_telemetry.py
```

SYNTHETIC endpoints only — not learner evidence.
