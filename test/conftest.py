#!/usr/bin/env python

import os

def pytest_addoption(parser):
    parser.addoption("--prepublish-branch", action="store", default="", help="Branch in ASmirnov-HORIS fork of the repo with most actual version of the site.")

def pytest_configure(config):
    os.environ["prepublish_branch"] = config.getoption("prepublish_branch")