#!/usr/bin/env python

import os
from datetime import datetime

import pytest

@pytest.mark.parametrize(('filename'), ["README.md", "LICENSE"])
def test_copyright_year(filename):
    expected_current_year = datetime.now().year
    copyright_prefix = "Copyright © "
    with open(filename) as f:
        for l in f:
            line = l.strip()
            if not line.startswith(copyright_prefix):
                continue
            years_range = line[len(copyright_prefix):len(copyright_prefix)+9]
            copyright_current_year = int(years_range.split("-")[1])
            assert expected_current_year == copyright_current_year
            break
