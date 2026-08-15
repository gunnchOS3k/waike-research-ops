# Week 9: Message schemas — /cmd_vel shaped fixtures without fleet claims

Ticket RB-5909: validate a cmd_vel-shaped JSON with linear.x and angular.z finite, and
frame_id='base_link'. Claiming a 50-robot Harbor fleet deploy fails.

NO_AI week. Consensus Ladder: observed = schema card; inferred = units m/s and rad/s;
still need = DDS/ROS distro pin (not claimed as production).

cmd_vel-shaped JSON needs finite linear_x/angular_z and frame_id=base_link.
fleet_claim=false. NaNs fail. NO_AI week: hand-author the schema. Production DDS/ROS
distro pins are not granted by schema vocabulary alone.

Hand-author RB-5909 cmd_vel JSON with finite linear_x, angular_z, and frame_id=base_link.
fleet_claim must be false; NaNs fail. NO_AI week forbids generative schema dumps.
Production DDS/ROS distro pins are not granted by vocabulary alone. Add a negative case
with angular_z=null and show the validator reject text the pier expects learners to cite.

Document a second negative for RB-5909: linear_x set to NaN while angular_z is finite, and show
that fleet_claim must remain false even if a slide deck claims fifty harbor robots. Cite the
schema card fields by name in the journal so the reject is reproducible without a GUI.

## Worked example

linear.x + angular.z finite; frame_id base_link; fleet_claim=false.
