# Test A - Config File
import os
if os.path.isfile("sysaudit.cfg"):
    print("PASS: Configuration file exists")
else:
    print("FAIL: Configuration file missing")
