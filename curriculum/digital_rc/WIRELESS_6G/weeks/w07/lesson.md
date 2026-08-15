# Week 7: AI-RAN control loop — gated policy, not magic autonomy

Ticket WR-4707: observe KPI window → propose MCS/PRB action → human gate → apply.
Submit observe_kpis, proposed_action, human_gate=true, auto_apply_without_gate=false.
Ungated auto-apply fails.

AI-RAN is research/systems with gates — not pier-wide 6G autonomy. NO_AI quiz week.
Consensus Ladder: observed = KPI CSV; inferred = actions need gates; still need =
closed-loop field trial evidence (not claimed).

Write the AI-RAN loop as four explicit fields: observe_kpis (list), proposed_action
containing MCS or PRB language, human_gate=true, auto_apply_without_gate=false.
Ungated reinforcement-learning theater fails the validator.

NO_AI quiz week still allows disclosed calculators on the lab JSON. Closed-loop field
trial evidence is not claimed; the pier remains RESEARCH_LAB_SCALE.

Ticket arithmetic checkpoint for WIRELESS_6G week 7: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

human_gate=true; auto_apply_without_gate=false; action names MCS or PRB.
