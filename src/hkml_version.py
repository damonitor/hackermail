#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0

import os

def get_version():
    pyproject = os.path.join(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))), 'pyproject.toml')
    in_project = False
    with open(pyproject) as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith('['):
                in_project = stripped == '[project]'
                continue
            if in_project and stripped.startswith('version'):
                return stripped.split('=', 1)[1].strip().strip('"')
    return 'unknown'

def main(args):
    print('hackermail (hkml) %s' % get_version())

def set_argparser(parser):
    pass
