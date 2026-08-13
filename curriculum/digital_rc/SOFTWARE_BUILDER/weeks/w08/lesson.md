# Week 8: Deploy and rollback on Device Lab compose

Deploy pins image digest sha256:… to local compose and writes rollback pointer to previous digest. Lab checks rollback_to != current and health healthy only after migrate=ok. Skipping migrate fails.

Physical flashing out of scope; Device Lab here is digital compose. Capstone preview: issue through deploy artifact path.

Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. 

## Worked example

current=sha256:aaa rollback_to=sha256:bbb migrate=ok health=healthy.
