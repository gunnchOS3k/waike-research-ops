# Objectives — ROBOTICS_CONTROL

## Program learning outcomes

_GAP: no numbered learning outcomes extracted from program file — use package week contracts._

## Week-level objectives (from package lessons)

### Week 1: HarborBot frames — SE(2) pose without cinematic hype
  - Complete the week contract: HarborBot frames — SE(2) pose without cinematic hype.
  - Reproduce worked example: theta=π/2, tool offset (0.2,0) → tool maps to pier axes with sin/cos.
  - HarborBot Bay ticket RB-5101: a diff-drive cart on taped pier coordinates.
### Week 2: 2R kinematics — reachability before torque myths
  - Complete the week contract: 2R kinematics — reachability before torque myths.
  - Reproduce worked example: L1=0.35, L2=0.30; point beyond 0.65 m → reachable=false.
  - Ticket RB-5202: planar 2R arm with L1=0.35 m, L2=0.30 m.
### Week 3: PID on a fixture plant — gains with anti-windup note
  - Complete the week contract: PID on a fixture plant — gains with anti-windup note.
  - Reproduce worked example: Compute u_last from fixture gains; document anti-windup note.
  - Ticket RB-5303: discrete PID on e=[1.0,0.6,0.2] with Kp=1.2, Ki=0.4, Kd=0.1, dt=0.1.
### Week 4: Trajectory limits — vmax/amax before cinematic paths
  - Complete the week contract: Trajectory limits — vmax/amax before cinematic paths.
  - Reproduce worked example: Distance 1.2 m, vmax 0.4, amax 0.5 → compute t_min; path_ok respects vmax.
  - Ticket RB-5404: move 1.2 m with vmax=0.4 m/s and amax=0.5 m/s².
### Week 5: Sensor noise — mean/std and reject wild outliers
  - Complete the week contract: Sensor noise — mean/std and reject wild outliers.
  - Reproduce worked example: Drop 3.50; cleaned_n=4; mean≈1.005.
  - Ticket RB-5505: lidar range samples [1.01,1.00,0.99,1.02,3.50] m.
### Week 6: E-stop policy — hard interrupt beats soft hope
  - Complete the week contract: E-stop policy — hard interrupt beats soft hope.
  - Reproduce worked example: motors_disabled, brake_engaged, resume_requires_human all true.
  - Ticket RB-5606: E-stop must assert motors_disabled=true, brake_engaged=true, and
resume_requires_human=true.
### Week 7: Diff-drive ICC — wheel speeds to body twist
  - Complete the week contract: Diff-drive ICC — wheel speeds to body twist.
  - Reproduce worked example: v=(r/2)*(ω_l+ω_r); ω=(r/B)*(ω_r-ω_l).
  - Ticket RB-5707: wheel base B=0.40 m, r=0.05 m, wheel rates ω_l, ω_r.
### Week 8: State estimation toy — fuse odom + range with covariance honesty
  - Complete the week contract: State estimation toy — fuse odom + range with covariance honesty.
  - Reproduce worked example: K=p/(p+r); x_hat = x_odom + K*(x_range-x_odom); no zero-cov lie.
  - Ticket RB-5808: scalar fuse x_odom and x_range with variances.
### Week 9: Message schemas — /cmd_vel shaped fixtures without fleet claims
  - Complete the week contract: Message schemas — /cmd_vel shaped fixtures without fleet claims.
  - Reproduce worked example: linear.x + angular.z finite; frame_id base_link; fleet_claim=false.
  - Ticket RB-5909: validate a cmd_vel-shaped JSON with linear.x and angular.z finite, and
frame_id='base_link'.
### Week 10: Capstone safety packet — E-stop + traj + fuse evidence
  - Complete the week contract: Capstone safety packet — E-stop + traj + fuse evidence.
  - Reproduce worked example: estop_ok true; labs_passed≥6; no_device_os_pr true.
  - Ticket RB-5910: assemble E-stop policy, traj limits, and fuse result digests.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
