#!/usr/bin/env python

import os

BUILD_DIR = "docs"
CNAME_PATH = "CNAME"

def test_cname_presence():
	cname_fullpath = os.path.join(BUILD_DIR, CNAME_PATH)
	assert os.path.isfile(cname_fullpath), "CNAME file isn't presented in the build directory"