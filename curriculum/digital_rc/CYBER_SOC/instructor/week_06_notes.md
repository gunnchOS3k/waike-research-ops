# CYBER_SOC — Shift-lead notes, week 6

**Board work:** A: From mail.harborpay.example, SPF via bounce.harborpay.example, DKIM d=harborpay.example → aligned → DMARC pass; B: From harborpay.example, SPF/DKIM pass for bulk-sender.example → not aligned → DMARC fail

**Desk drill:** replay lab_soc_dmarc_align against a log with one line changed.

**Watch for:** Treating a subdomain sender as misaligned under relaxed DMARC.
