# Week 9: Media sanitization — Clear, Purge, or Destroy before a device leaves

ISH-4909 is the second NO_AI week, because a sanitization decision has to be yours. Donated machines arrive full of strangers' lives, and the bench's promise is that nothing leaves with them. NIST Special Publication 800-88 frames the choice with three words. Clear uses ordinary commands to overwrite user-addressable storage, enough when the device stays inside the organisation. Purge uses methods that defeat laboratory recovery, such as the drive's own secure-erase or cryptographic-erase commands, and is the floor when a device leaves your control through donation, sale, or a returned lease. Destroy means the media cannot be reused: shredding, disintegrating, or incinerating, and it is the only answer for a drive that has failed and will not accept commands. Solid-state drives remap blocks behind the scenes, so overwriting the visible space can leave old data in spare areas; rely on the drive's purge commands. Every decision ends with verification and a certificate recording the serial number, method, date, and who did it. A quick format is none of the three.

## Worked example

RB-1001 HDD reuse_internal → Clear; RB-1002 SSD leave_org → Purge; RB-1003 failed SSD → Destroy; RB-1004 HDD leave_org → Purge; each verified with a certificate ID
