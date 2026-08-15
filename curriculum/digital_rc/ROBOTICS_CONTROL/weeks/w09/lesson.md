# Week 9: Message schemas — /cmd_vel shaped fixtures without fleet claims

Ticket RB-5909: validate a cmd_vel-shaped JSON with linear.x and angular.z finite, and
frame_id='base_link'. Claiming a 50-robot Harbor fleet deploy fails.

NO_AI week. Consensus Ladder: observed = schema card; inferred = units m/s and rad/s;
still need = DDS/ROS distro pin (not claimed as production).

cmd_vel-shaped JSON needs finite linear_x/angular_z and frame_id=base_link.
fleet_claim=false. NaNs fail. NO_AI week: hand-author the schema. Production DDS/ROS
distro pins are not granted by schema vocabulary alone.

Ticket arithmetic checkpoint for ROBOTICS_CONTROL week 9: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

linear.x + angular.z finite; frame_id base_link; fleet_claim=false.
