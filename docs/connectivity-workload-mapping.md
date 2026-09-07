# Connectivity Workload Mapping

## WAIKE Activity to Research Workload Mapping

| WAIKE activity | Research workload | Device link | 6G metric |
|----------------|------------------|-------------|-----------|
| Coursework | Learn profile | Student 14.5" | throughput, continuity, accessibility |
| Mobile lessons/demos | Mobile profile | Handheld Hybrid | mobility, handover, jitter |
| Code/build/deploy | Create profile | DS-XL Coder | local edge, sync delay, peer transfer |
| Kinesthetic labs | Sense profile | Edge IO Wearables | latency, haptics, safety |
| Service projects | Community profile | All devices | availability, reliability, documentation |
| Portfolio/demo nights | Presentation profile | Student + Handheld | uplink, video, sync, resilience |
| Device clinics | Support profile | Student + DS-XL | diagnostics, local records, privacy |

## Workload Profile Definitions

### Learn profile
- Sustained download (video, documents, LMS)
- Periodic upload (submissions, quizzes)
- Session duration: 30–120 minutes
- Interruption tolerance: low
- Accessibility: screen reader, captioning, low-bandwidth alternatives

### Mobile profile
- Bursty access (short interactions, notifications, field capture)
- Frequent handover between Wi-Fi and cellular
- Session duration: 5–30 minutes
- Interruption tolerance: medium
- Location variability: high

### Create profile
- Heavy local compute (compilation, inference, container ops)
- Periodic sync (git push, artifact upload, peer share)
- Session duration: 60–240 minutes
- Interruption tolerance: high for network (local-first)
- Peer traffic: device-to-device file transfer

### Sense profile
- Continuous sensor input (IMU, environmental, haptic triggers)
- Ultra-low-latency feedback loop
- Session duration: 15–60 minutes
- Interruption tolerance: none for safety-critical
- Body-area network traffic: high frequency, small packets

### Community profile
- Mixed device ensemble (all four devices active)
- Collaborative access patterns
- Session duration: variable
- Documentation and capture: photos, video, notes

### Presentation profile
- High uplink (screen share, video stream)
- Low-latency interaction (Q&A, real-time feedback)
- Session duration: 15–60 minutes
- Interruption tolerance: very low (live audience)

### Support profile
- Diagnostic data access (device logs, network state)
- Local record keeping (repair history, configuration)
- Privacy-sensitive (device owner data)
- Network requirement: local-only acceptable
