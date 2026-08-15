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

On WR-4707, enumerate observe_kpis as concrete CSV column names (bler, prb_util, snr_p50)
before proposing MCS or PRB moves. Document the human gate as a named pier operator role,
not a checkbox theater. Auto-apply without that gate must remain false in every submitted
JSON variant the class practices. Compare one gated proposal against an ungated fantasy
loop and mark which fields the validator rejects. Keep AI-RAN vocabulary at RESEARCH_LAB_SCALE;
do not imply pier-wide closed-loop autonomy from this ticket alone.

## Worked example

human_gate=true; auto_apply_without_gate=false; action names MCS or PRB.
