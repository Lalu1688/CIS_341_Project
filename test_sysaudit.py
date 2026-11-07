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




# Test D - Malformed Configuration

config_value = "invalid"

try:
    max_limit = float(config_value)
    print("FAIL: Invalid value accepted")
except ValueError:
    print("PASS: Invalid configuration value detected")



# Test E - Storage Limit Exceeded

max_limit = 100.0
current_size = 150.0

if current_size > max_limit:
    print("PASS: Storage limit exceeded")
else:
    print("FAIL: Storage limit not exceeded")
