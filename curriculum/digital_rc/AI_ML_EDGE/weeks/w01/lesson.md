# Week 1: EdgeForge Bench — Python tensors as civic tables

The EdgeForge Bench in Gary is a rolling rack of three Coral-class USB accelerators and a battered ThinkPad that only sees the civic Wi-Fi. Week 1 is not 'learn Python.' It is naming columns so a sensor CSV becomes a matrix you can defend to a librarian. Ticket EF-2101 ships a 480-row occupancy CSV: timestamp_iso, zone_id, people_count, rssi_dbm. Beginners paste the file into a notebook and celebrate a DataFrame shape. Operators ask which rows are training candidates and which are the midnight janitor sweep that always reads people_count=0 for forty minutes.

Python here is a broom, not a religion. You will use pathlib, csv.DictReader, and a hand-rolled mean — not a mystery import that hides a download. The lab rejects a submission that claims train_n without showing the split math. Privacy starts now: zone_id is a letter (A/B/C), never a camera MAC, never a patron face embedding.

Consensus Ladder for EF-2101: observed = 480 rows with four columns; inferred = midnight zeros are cleaning, not empty buildings; still need = whether zone B's RSSI drop correlates with AP reboot logs (out of scope this week).

Worked numbers: 480 rows, hold out last 96 (20%) for validation by time order, not shuffle — civic occupancy is autocorrelated. Training rows = 384. If someone shuffles first, midnight cleaning contaminates both folds and the F1 will lie.

Name the failure mode before you touch pandas. On EF-2101 the idle janitor sweep is a remembered pattern in time, not a class label. If you shuffle, you teach the model that midnight zeros belong in daytime folds, and the F1 you celebrate is a leak costume.

Operators speak paths: `fixtures/ef2101/occupancy.csv`, then `train_n` and `val_n` as integers you can defend on a whiteboard. The lab marks missing split fields; it does not grade a notebook theme. Zone letters A/B/C are the only spatial vocabulary — never a camera serial, never an embedding that could re-identify a patron.

When a volunteer asks to 'just use sklearn train_test_split,' answer with the autocorrelation clock: last-keystroke times cluster. Time order is the civic control, the same way the library idle timer is a shared-kiosk control rather than a personal preference.

## Worked example

480 rows × 0.80 = 384 train; 96 validation by time order (not shuffle).
