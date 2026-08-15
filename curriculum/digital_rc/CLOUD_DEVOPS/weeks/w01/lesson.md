# Week 1: ForgeCloud — Linux permissions before the fancy YAML

ForgeCloud Platform starts on a Linux bastion that deploys nothing until permissions make sense. Ticket FC-4101 shows a deploy key file mode 0666 — world writable. You will compute the correct mode 0600 and refuse to continue CI until the lab's mode check passes. Cloud YAML cannot save a secret that every login can rewrite.

deploy_key mode 0666 → must be 0600; owner read/write only.

Permissions before YAML. A deploy key at 0666 is world writable; ForgeCloud requires 0600 (octal 384) and world_writable=false before any pipeline talk.

Cloud manifests cannot redeem a secret every login can rewrite. Bastion discipline is the first SRE muscle: name the mode, fix the mode, then consider containers.

NO_AI week for the mode arithmetic when tagged. Journal the risk in one line: anyone with directory listing access can replace the key material and impersonate deploys.

## Worked example

0666 world-writable deploy key fails; 0600 passes.
