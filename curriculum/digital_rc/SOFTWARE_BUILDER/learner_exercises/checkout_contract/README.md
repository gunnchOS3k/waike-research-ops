# Checkout contract worked example

New to programming? Start with the downloadable **Your first program** guide and its `capacity.py` / `test_capacity.py` files, then return here.

Prerequisites: Python 3.11+ on a computer you control, a text editor and ability to open a terminal in a folder. Uses Python's standard library only. No network service, packages, accounts or real library data are needed.

Download `checkout.py` and `test_checkout.py` into the same empty folder. From that folder run:

```
python3 -m unittest -v test_checkout.py
```

On Windows where the Python launcher is installed, use `py -3 -m unittest -v test_checkout.py`. Expected result: six tests pass. A missing Python command means the runtime prerequisite is unmet; do not copy commands from an unknown download site. A module import error usually means you ran from the wrong folder or did not save both files with `.py` extensions.

Read each assertion and predict its result before running. Then deliberately change the reader authorization check to allow POST, rerun and observe the failed denial test. Restore the original condition and rerun. Save the before/after result; a screenshot of a green test run alone does not show that you understand why it passed.

Independent work: add a second fictional item and tests showing that checking out the first does not change the second. Add a test for an unsupported method and a separate test for an unrecognized role. Explain why a user-supplied role string would be unsafe in a real web service. Do not use this exercise as an authentication or production database implementation.

This is a local worked example, not execution of the canonical ForgeDesk infrastructure labs. Those require their documented artifact schemas and authorized environment. AI assistance contributed to the example and tests. Human technical and educational acceptance remains pending. Source inherits the repository's software license; publication and third-party rights remain separately reviewed.
