# Week 1: Auth log anatomy — failures, sources, and the success that follows

Ticket SOC-2101 lands at 01:20 on the Night Shift Desk: eight lines from the bastion host's sshd log and a request to say whether anything matters. Read a log line left to right as a sentence. The timestamp says when, the host and process say where, and the message says what happened to whom from which address. In this fixture 203.0.113.45 fails three times as root, 198.51.100.7 tries the made-up accounts admin and oracle twice, and 192.0.2.10 fails once right after the user naiya logged in with her key from the same machine. Counting failures per source is the start, not the finding. The line that changes the night is the last one: Accepted password for root from 203.0.113.45, seconds after that address failed. A success that follows a run of failures from the same source is the pattern analysts escalate, because it can mean a guessed password. Naiya's typo after a good key login is noise you note and move past. All addresses here come from documentation ranges, so nobody's real server appears in the course, and you never paste a live customer log into a chat tool to save time.

## Worked example

203.0.113.45 failed 3×, 198.51.100.7 failed 2×, 192.0.2.10 failed 1×; Accepted password for root from 203.0.113.45 at 01:15:31 → escalate
