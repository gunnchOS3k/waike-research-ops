# WAIKE Taxonomy Reconciliation

Generated (UTC): `2026-09-02T19:11:17Z`
Source commit: `b44a45e15bf2ab840ad18701b65430a10f3a7623`
Registry hash (sha256): `7c72905b45ca2bbe55650b89ef0ccd66ae15269be84b5cf18a2b89e896d9c4ac`

## Exact counts

- Canonical tracks: **18**
- Historical aliases: **32**
- Digital RC package dirs on disk (`ls curriculum/digital_rc`): **16**
- Package mappings: **4**
- Unresolved collisions: **2**
- Mismatches recorded: **3**
- Similar titles not aliased: **3**

## Canonical 18 tracks

| track_id | academy | extension | maturity | aliases |
|---|---|---|---|---|
| `DIGITAL_CONFIDENCE` | `ACADEMY_IT` | `FOUNDATION` | `covered_via_shared_package` | `WAIKE_COURSE_DIGITAL_CONFIDENCE`, `digital_confidence` |
| `IT_SUPPORT_HARDWARE` | `ACADEMY_IT` | `FOUNDATION` | `covered_via_shared_package` | `WAIKE_COURSE_IT_SUPPORT_HARDWARE`, `it_support_hardware` |
| `SOFTWARE_BUILDER` | `ACADEMY_SOFTWARE` | `FOUNDATION` | `digital_rc_present` | `WAIKE_COURSE_SOFTWARE_BUILDER`, `software_builder` |
| `NETWORKING_INFRA` | `ACADEMY_NETWORKING` | `FOUNDATION` | `covered_via_historical_package_id` | `WAIKE_COURSE_NETWORKING_INFRA`, `COMPUTER_NETWORKING` |
| `CYBER_SOC` | `ACADEMY_CYBER` | `FOUNDATION` | `covered_via_historical_package_id` | `WAIKE_COURSE_CYBER_SOC`, `CYBERSECURITY`, `cybersecurity` |
| `DATA_DASHBOARDS` | `ACADEMY_SOFTWARE` | `FOUNDATION` | `digital_rc_present` | `WAIKE_COURSE_DATA_DASHBOARDS` |
| `AI_ML_EDGE` | `ACADEMY_SOFTWARE` | `ADVANCED_EXTENSION` | `digital_rc_present` | `WAIKE_COURSE_AI_ML_EDGE`, `ai_ml_edge` |
| `EMBEDDED_PROTOTYPING` | `ACADEMY_HARDWARE` | `ADVANCED_EXTENSION` | `digital_rc_present` | `WAIKE_COURSE_EMBEDDED_PROTOTYPING`, `embedded_prototyping` |
| `WIRELESS_6G` | `ACADEMY_NETWORKING` | `ADVANCED_EXTENSION` | `digital_rc_present` | `WAIKE_COURSE_WIRELESS_6G` |
| `PM_AGILE_LSS` | `ACADEMY_PROCESS_PM` | `FOUNDATION` | `digital_rc_present` | `WAIKE_COURSE_PM_AGILE_LSS`, `pm_agile_lss` |
| `GAME_DEV_INTERACTIVE` | `ACADEMY_SOFTWARE` | `ADVANCED_EXTENSION` | `digital_rc_present` | `WAIKE_COURSE_GAME_DEV_INTERACTIVE`, `game_dev_interactive` |
| `SEVEN_GC_APPRENTICESHIP` | `ACADEMY_SOFTWARE` | `RESEARCH_APPRENTICESHIP` | `program_shell_only` | `WAIKE_COURSE_SEVEN_GC_APPRENTICESHIP`, `seven_gc_apprenticeship` |
| `CLOUD_DEVOPS` | `ACADEMY_SOFTWARE` | `ADVANCED_EXTENSION` | `digital_rc_present` | `WAIKE_COURSE_CLOUD_DEVOPS`, `cloud_devops` |
| `COMM_PD_ETHICS` | `ACADEMY_PROF_DEV` | `FOUNDATION` | `digital_rc_present` | `WAIKE_COURSE_COMM_PD_ETHICS` |
| `ROBOTICS_CONTROL` | `ACADEMY_HARDWARE` | `ADVANCED_EXTENSION` | `digital_rc_present` | `WAIKE_COURSE_ROBOTICS_CONTROL`, `robotics_control` |
| `GUNNCHOS_PRODUCT_LAB` | `ACADEMY_HARDWARE` | `ADVANCED_EXTENSION` | `digital_rc_present` | `WAIKE_COURSE_GUNNCHOS_PRODUCT_LAB` |
| `HARDWARE_ENGINEERING` | `ACADEMY_HARDWARE` | `FOUNDATION` | `covered_via_shared_package` | `WAIKE_COURSE_HARDWARE_ENGINEERING`, `hardware_engineering` |
| `DATA_VIZ_BI` | `ACADEMY_SOFTWARE` | `ADVANCED_EXTENSION` | `digital_rc_present` | `WAIKE_COURSE_DATA_VIZ_BI` |

## Package mappings (not aliases when multi-track)

- `GENERAL_IT` → ['DIGITAL_CONFIDENCE', 'IT_SUPPORT_HARDWARE'] (shared_digital_rc_package)
- `COMPUTER_NETWORKING` → ['NETWORKING_INFRA'] (historical_package_id)
- `CYBERSECURITY` → ['CYBER_SOC'] (historical_package_id)
- `HARDWARE_ENGINEERING` → ['HARDWARE_ENGINEERING', 'EMBEDDED_PROTOTYPING'] (shared_digital_rc_package)

## Digital RC packages on disk

`AI_ML_EDGE`, `CLOUD_DEVOPS`, `COMM_PD_ETHICS`, `COMPUTER_NETWORKING`, `CYBERSECURITY`, `DATA_DASHBOARDS`, `DATA_VIZ_BI`, `EMBEDDED_PROTOTYPING`, `GAME_DEV_INTERACTIVE`, `GENERAL_IT`, `GUNNCHOS_PRODUCT_LAB`, `HARDWARE_ENGINEERING`, `PM_AGILE_LSS`, `ROBOTICS_CONTROL`, `SOFTWARE_BUILDER`, `WIRELESS_6G`

## Historical IDs retained as aliases

`COMPUTER_NETWORKING`, `CYBERSECURITY`, `WAIKE_COURSE_AI_ML_EDGE`, `WAIKE_COURSE_CLOUD_DEVOPS`, `WAIKE_COURSE_COMM_PD_ETHICS`, `WAIKE_COURSE_CYBER_SOC`, `WAIKE_COURSE_DATA_DASHBOARDS`, `WAIKE_COURSE_DATA_VIZ_BI`, `WAIKE_COURSE_DIGITAL_CONFIDENCE`, `WAIKE_COURSE_EMBEDDED_PROTOTYPING`, `WAIKE_COURSE_GAME_DEV_INTERACTIVE`, `WAIKE_COURSE_GUNNCHOS_PRODUCT_LAB`, `WAIKE_COURSE_HARDWARE_ENGINEERING`, `WAIKE_COURSE_IT_SUPPORT_HARDWARE`, `WAIKE_COURSE_NETWORKING_INFRA`, `WAIKE_COURSE_PM_AGILE_LSS`, `WAIKE_COURSE_ROBOTICS_CONTROL`, `WAIKE_COURSE_SEVEN_GC_APPRENTICESHIP`, `WAIKE_COURSE_SOFTWARE_BUILDER`, `WAIKE_COURSE_WIRELESS_6G`, `cybersecurity`

## Unresolved collisions (fail-closed)

- `GENERAL_IT`: shared_digital_rc_package_covers_two_tracks → package_mappings_only_not_alias
- `general_it`: snake_of_multi_track_package_not_alias → left_unresolved_fail_closed

## Mismatches

- `shared_package_also_has_standalone_track_package`: EMBEDDED_PROTOTYPING also has curriculum/digital_rc/EMBEDDED_PROTOTYPING; package_mappings records multi-cover without aliasing.
- `gap_ledger_stale_vs_disk`: WAIKE_FULL_TAXONOMY_GAP_LEDGER.json marked NETWORKING_INFRA/CYBER_SOC BELOW_BAR; disk has COMPUTER_NETWORKING and CYBERSECURITY packages mapping 1:1.
- `gap_ledger_package_count_stale`: Ledger predates EMBEDDED_PROTOTYPING and GUNNCHOS_PRODUCT_LAB package dirs.

## Similar titles intentionally NOT aliased

- `networking` (~`NETWORKING_INFRA`): lessons/by_course/networking exists but is not exact snake of track_id or 1:1 historical package id; not invented
- `software_engineering` (~`SOFTWARE_BUILDER`): similar title/folder; no explicit track_id evidence
- `data_visualization_bi` (~`DATA_VIZ_BI`): similar folder name; not exact snake of DATA_VIZ_BI

## What this PR fixes

- Canonical 18-track registry with deterministic uuid5 stable IDs
- Evidence-only historical alias map + fail-closed resolve_track_id
- Explicit package_mappings for multi-track and historical package IDs
- Deterministic consumer export with registry_hash
- Reconciliation reports separating contract work from remaining content gaps

## Remaining content work (out of contract scope)

- SEVEN_GC_APPRENTICESHIP still has no digital_rc package (program shell only)
- DIGITAL_CONFIDENCE and IT_SUPPORT_HARDWARE remain shared under GENERAL_IT (no standalone packages)
- Package version fields are null until versioned package manifests exist
- Track-level prerequisites arrays are empty pending evidence-backed prerequisite graph
- Stale gap ledger should be refreshed in a follow-up content/ops packet
- Similar-title lesson folders (networking, software_engineering, …) remain unresolved by design
