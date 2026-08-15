# Week 5: Sensor noise — mean/std and reject wild outliers

Ticket RB-5505: lidar range samples [1.01,1.00,0.99,1.02,3.50] m. Compute mean/std after
dropping values beyond 1.5×IQR or a hard gate >2.0 m. Lab checks cleaned_n, mean, outlier_dropped.

Consensus Ladder: observed = samples; inferred = 3.50 is outlier for pier aisle; still need =
calibrated bias. Failure: trusting raw max as truth.

Operators keep a numbered ticket trail for w5-lab_sensor_noise and refuse noun-swapped decks from other academies. Detail mark w5-lab_sensor_noise-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w5-lab_sensor_noise-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w5-lab_sensor_noise-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w5-lab_sensor_noise-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w5-lab_sensor_noise-4.

## Worked example

Drop 3.50; cleaned_n=4; mean≈1.005.
