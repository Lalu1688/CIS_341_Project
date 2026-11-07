# Test A - Config File
import os
if os.path.isfile("sysaudit.cfg"):
    print("PASS: Configuration file exists")
else:
    print("FAIL: Configuration file missing")


# Test B - Missing Config File

if not os.path.exists("missing.cfg"):
    print("PASS: Test file is missing")
else:
    print("FAIL: Test file exists")
