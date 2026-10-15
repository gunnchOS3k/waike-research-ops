# Week 5: Reliability on an unreliable wire — sequences, ACKs, AIMD on paper

TCP (current spec RFC 9293) pretends the wire is reliable by numbering bytes and refusing to live on hope. Sequence 1000, payload 200 bytes, ACK 1200 means 'I have everything before 1200.' If ACK 1000 returns, none of that payload is safe yet.

The three-way handshake is not a personality test. SYN, SYN-ACK, ACK. Data before the handshake completes is a bug in your mental model (or an experimental Fast Open you will not implement here).

Congestion control in this course is AIMD arithmetic: cwnd 10, loss, halve to 5, then +1 per RTT. You will compute a table for 8 RTTs. You will not port a C++ TCP stack. That is the CS144 shape we refuse to copy and the WAIKE shape we can actually grade offline.

Flow control (rwnd) is the receiver's remaining belly. Congestion control is the network's remaining belly. Mixing those two words is how people tune the wrong knob.

## Concept and scope

TCP provides an ordered byte stream to applications using mechanisms including sequence numbers, acknowledgments and retransmission. Acknowledgment of bytes is not a guarantee that an application saved them durably. Congestion control addresses network load; receive-window flow control addresses receiver capacity.

## Guided practice

On paper, label three non-overlapping data ranges: bytes 0–99, 100–199 and 200–299 in a simplified relative sequence space. Suppose only the first and third arrive. Expected result: a cumulative acknowledgment cannot claim the missing contiguous range has arrived. Explain why selective acknowledgment, when used, can communicate additional receipt information without making the stream gap disappear.

## Independent evidence

Trace a retransmission and distinguish duplicate arrival from duplicate application delivery. State that your diagram omits connection setup, sequence-number wrap and timers. Do not infer real throughput or congestion behavior from this paper trace.

## Worked example

seq=1000 len=200 → ACK 1200 on full receipt. cwnd 10, loss → 5, then 6,7,8... on additive increase per RTT without further loss.
