# Objectives — AI_ML_EDGE

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: EdgeForge Bench — Python tensors as civic tables
  - Complete the week contract: EdgeForge Bench — Python tensors as civic tables.
  - Reproduce worked example: 480 rows × 0.80 = 384 train; 96 validation by time order (not shuffle).
  - The EdgeForge Bench in Gary is a rolling rack of three Coral-class USB accelerators and a battered ThinkPad that only sees the civic Wi-Fi.
### Week 2: Supervised labels — desk occupancy as a class, not a vibe
  - Complete the week contract: Supervised labels — desk occupancy as a class, not a vibe.
  - Reproduce worked example: TP=40 FP=10 FN=5 → precision=0.800 recall=0.889 F1≈0.842.
  - Supervised learning on EdgeForge means a label you can argue about.
### Week 3: Unsupervised clusters — failure modes without a teacher
  - Complete the week contract: Unsupervised clusters — failure modes without a teacher.
  - Reproduce worked example: p=(55,2000,2) closer to B=(70,1200,5) with Manhattan 818 vs 1017.
  - Not every EdgeForge ticket has a label.
### Week 4: Evaluation curves — thresholds are staffing decisions
  - Complete the week contract: Evaluation curves — thresholds are staffing decisions.
  - Reproduce worked example: t=0.60 → TPR=0.75 FPR≈0.167 (≤0.20 constraint).
  - Week 4 turns the busy classifier into a curve.
### Week 5: Overfitting — when train glory means val shame
  - Complete the week contract: Overfitting — when train glory means val shame.
  - Reproduce worked example: train_acc=0.99 val_acc=0.61 → gap=0.38 (≥0.25 triggers mitigation note).
  - Ticket EF-2502 shows a student model with train_acc=0.99 and val_acc=0.61.
### Week 6: Feature windows — telemetry that respects time
  - Complete the week contract: Feature windows — telemetry that respects time.
  - Reproduce worked example: w=5 at index 4 → mean(10,12,11,13,12)=11.6.
  - Feature engineering on EdgeForge is mostly windows.
### Week 7: Tiny neural net — forward pass without mythology
  - Complete the week contract: Tiny neural net — forward pass without mythology.
  - Reproduce worked example: Published fixture forward pass yields y_hat≈0.731 (±1e-3).
  - Neural foundations on EdgeForge stay tiny: one hidden layer, two inputs (windowed rssi, hour_norm), two hidden units, one sigmoid output.
### Week 8: Deploy + inference — scoring JSON on the rack
  - Complete the week contract: Deploy + inference — scoring JSON on the rack.
  - Reproduce worked example: scores 0.62/0.40/0.81 at t=0.55 → labels 1/0/1 with matching digest.
  - Deployment on EdgeForge is a scored JSON bundle pinned by sha256, not a demo laptop left unlocked.
### Week 9: Quantization + edge budget — int8 vs desk latency
  - Complete the week contract: Quantization + edge budget — int8 vs desk latency.
  - Reproduce worked example: 1000 params: fp32=4000B int8=1000B ratio=0.25; latency 12ms ≤15 → ok.
### Week 10: RAG, privacy, responsibility — retrieve without leaking patrons
  - Complete the week contract: RAG, privacy, responsibility — retrieve without leaking patrons.
  - Reproduce worked example: top_k hits R12,R19; redactions=2; biometric_claim=false.
  - Capstone week: a tiny RAG over EdgeForge runbooks.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
