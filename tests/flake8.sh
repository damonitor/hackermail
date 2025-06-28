#!/bin/bash
# SPDX-License-Identifier: GPL-2.0

set -e

bindir=$(dirname "$0")
# this file is at /tests/ of the repo
src_dir="$bindir/../src/"

if ! pip3 show flake8 > /dev/null
then
	echo "flake8 not found. skip."
	exit 0
fi

if ! python3 -m flake8 "$src_dir" --select=F821,E999 --show-source
then
	echo "linter failed"
	exit 1
fi
