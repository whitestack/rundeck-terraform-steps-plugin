#!/usr/bin/env python3

# terraform plan
import argparse
import os
import shlex
import subprocess
import sys

parser = argparse.ArgumentParser(description='Creates an execution plan')
parser.add_argument('path', help='Terraform project path')
args = parser.parse_args()

command = ["terraform", "-chdir=" + args.path, "plan"]

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
