# Week 5: Privacy BOM — field inventory without PII

gunnchOS Product Lab Bench ticket GPL-5505: Privacy BOM — field inventory without PII. Privacy BOM digital inventory; no biometric claim. PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. Empty {} fails. A file whose body is only PASS raises. Show computed JSON fields; GUI screenshots are not acceptance. Distinct from SOFTWARE_BUILDER ForgeDesk — this course owns product/compat/privacy/CI contract. Journal GPL-5505: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs. The privacy BOM lists each sensor or data field with its purpose, retention period and whether it leaves the device; it names categories, never sample values, and a 30-day retention promise needs a tested deletion job.

## Worked example

fields=[camera,mic,location], pii_in_bom=false, retention_days=30
