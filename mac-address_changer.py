#!/usr/bin/env python3

import subprocess
import sys


def mac_address():
    subprocess.run(["ifconfig"],shell=True)


mac_address()
