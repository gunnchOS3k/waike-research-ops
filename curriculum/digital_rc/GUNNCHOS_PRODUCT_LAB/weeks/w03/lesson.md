# Week 3: Checkout flow — ticket states and handoff

gunnchOS Product Lab Bench ticket GPL-5303: Checkout flow — ticket states and handoff. Model checkout FSM without opening unmerged device-os PRs. PHYSICAL_PENDING covers soldering, OTA, and carrier claims unless EVT evidence exists. Zephyr/KiCad/gunnchOS docs are PUBLIC_REFERENCE_ONLY — original WAIKE fixture wording only. Empty {} fails. A file whose body is only PASS raises. Show computed JSON fields; GUI screenshots are not acceptance. Distinct from SOFTWARE_BUILDER ForgeDesk — this course owns product/compat/privacy/CI contract. Journal GPL-5303: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs. Journal GPL-5303: restate the worked numbers, name one claim you refuse (commercial standardized 6G, vendor cert grant, unmerged device-os PR, fabricated field trial), and keep prose specific to this week's lab_id and ticket IDs.

## Worked example

states=[requested,approved,checked_out,returned], orphan_state=false
