# Week 4: Storage, snapshots, and the Friday 16:00 panic

The civic volume is 256 GiB. Used 180 GiB. Reserved 12 GiB for snapshots. The desk policy demands 15% free because Windows updates and browser profiles balloon without asking. Free = 256-180-12 = 64 GiB, which is 25% — you pass today. If used climbs to 220 GiB, you fail the policy before the disk is 'full,' and that is the point of a quota.

Backup is a restore you have practiced. A `.tgz` that nobody has extracted is a rumor. The lab hashes the tree, archives, restores, and hashes again. If you exclude `ticket_4417.txt` because it 'looks temporary,' the patron essay is gone.

The 3-2-1 strategy keeps three copies of important data on two media types, with one copy offsite. The desk volume and a local USB copy do not satisfy the offsite part. An encrypted copy in the same building can remain vulnerable to the same incident. Select an authorized separate location and test recovery, including access to encryption keys.

PII still does not belong in the archive. The lab fails if you add `ssn.txt`. Backup is not a place to hide documents you would not leave on the desk.

## Learn the distinction

A snapshot captures state within a storage system. Its survival depends on where its data is stored and how it is managed. A backup is a separately recoverable copy; recovery must be tested. Synchronization can propagate an accidental deletion and therefore is not automatically a versioned backup. A matching SHA-256 digest checks equality of the compared bytes; it does not prove that the original file is safe, correct or complete.

## Guided practice: restore without overwriting

1. Make a temporary practice directory containing two fictional text files. Record their names and exact contents.
2. Copy them into a second directory. Change one original file after copying.
3. Restore from the copy into a third, empty directory. Never restore over your only original during this exercise.
4. Compare each restored file against the recorded pre-change content. If you use a hashing tool, record its name and hash algorithm.
5. Deliberately omit one file in a second trial. Confirm that checking only one matching hash misses the absent file. Record a complete file inventory as well.

Expected result: the first restore reproduces both earlier files. The second trial reveals an incomplete backup even when the included file matches. If the restore fails, preserve the existing copies and diagnose the selected source and destination paths before retrying.

## Independent evidence

For a fictional household, propose three copies, two storage media types and one geographically separate copy. Identify who can restore it, what happens if Internet access fails, and how encryption keys will remain recoverable. Do not upload real private files for this assignment.

## Check your reasoning

A second machine in the same building is off-device but not offsite. It may help with one disk failure while remaining vulnerable to the same fire or flood. For the 256 GiB fixture, a 15% reserve policy is a configured classroom criterion, not a universal operating-system requirement.

## Worked example

size=256GiB used=180 reserved=12 → free=64 GiB → 64/256=0.25 ≥ 0.15. SHA256 of source tree must equal SHA256 of restored tree.
