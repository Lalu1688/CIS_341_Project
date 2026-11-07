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


# Test C - Invalid Path

audit_dir = "/invalid_directory"

if not os.path.isdir(audit_dir):
    print("PASS: Invalid directory detected")
else:
    print("FAIL: Directory exists")# Test C - Invalid Path

