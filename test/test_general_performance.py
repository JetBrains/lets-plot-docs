#!/usr/bin/env python

import os

BUILD_DIR = "docs"

def test_cname():
    CNAME_PATH = "CNAME"
    CNAME_CONTENT = "lets-plot.org"
    cname_fullpath = os.path.join(BUILD_DIR, CNAME_PATH)
    assert os.path.isfile(cname_fullpath), "CNAME file isn't presented in the build directory"
    with open(cname_fullpath, 'r') as f:
        assert f.read() == CNAME_CONTENT

def test_sitemap():
    SITEMAP_PATH = "sitemap.xml"
    sitemap_fullpath = os.path.join(BUILD_DIR, SITEMAP_PATH)
    assert os.path.isfile(sitemap_fullpath), "sitemap.xml file isn't presented in the build directory"