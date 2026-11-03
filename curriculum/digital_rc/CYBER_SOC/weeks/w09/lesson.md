# Week 9: Shift metrics — MTTD, MTTR, and the median that resists one bad night

SOC-2909 asks how the week went, in numbers management will read. Mean time to detect is the average gap between when something happened and when the desk noticed. The four incidents took 12, 45, 5 and 70 minutes to detect, so MTTD is 33 minutes. Mean time to resolve, measured here from detection to resolution, averages 78, 65, 35 and 150 minutes to 82. Define the start and end points in the report, because some teams measure resolution from occurrence and their numbers are not comparable with yours. One slow detection, the seventy-minute ransomware case, pulls the mean up; the median of the four detection times is 28.5 minutes and tells a steadier story about a typical night. Report both, and name the outlier instead of hiding it, since that is the incident the next tuning effort should study. Four incidents are a tiny sample. A dashboard that celebrates a five-minute drop in MTTD between two such weeks is reporting noise, so the course asks for the numbers and a sentence about how much they can bear.

## Worked example

time to detect = 12, 45, 5, 70 min → MTTD 33, median 28.5; time to resolve from detection = 78, 65, 35, 150 → MTTR 82
