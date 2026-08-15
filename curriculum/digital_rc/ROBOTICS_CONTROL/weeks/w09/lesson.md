# Week 9: Message schemas — /cmd_vel shaped fixtures without fleet claims

Ticket RB-5909: validate a cmd_vel-shaped JSON with linear.x and angular.z finite, and
frame_id='base_link'. Claiming a 50-robot Harbor fleet deploy fails.

NO_AI week. Consensus Ladder: observed = schema card; inferred = units m/s and rad/s;
still need = DDS/ROS distro pin (not claimed as production).

Operators keep a numbered ticket trail for w9-lab_cmd_vel_schema and refuse noun-swapped decks from other academies. Detail mark w9-lab_cmd_vel_schema-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w9-lab_cmd_vel_schema-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w9-lab_cmd_vel_schema-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w9-lab_cmd_vel_schema-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w9-lab_cmd_vel_schema-4.

## Worked example

linear.x + angular.z finite; frame_id base_link; fleet_claim=false.
