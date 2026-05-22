#!/usr/bin/env python3

# terraform destroy
import os
import shlex
import subprocess
import sys

path = sys.argv[1] if len(sys.argv) > 1 else ''
if not path:
    print("Error: Terraform path required", file=sys.stderr)
    sys.exit(2)

command = ["terraform", "-chdir=" + path, "destroy", "-auto-approve"]

extra = os.environ.get('RD_CONFIG_EXTRA_ARGS', '').strip()
if extra:
    command += shlex.split(extra)

try:
    result = subprocess.run(command)
    sys.exit(result.returncode)
except OSError as e:
    print(f"Command error: {e}", file=sys.stderr)
    sys.exit(1)
# Done
