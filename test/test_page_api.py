#!/usr/bin/env python

import inspect
import warnings

import pytest
from bs4 import BeautifulSoup

import lets_plot as lp
from lets_plot.bistro.im import *
from lets_plot.bistro.corr import *
from lets_plot.bistro.qq import *
from lets_plot.geo_data import *

from .parser import page_parser
from .generator import generate_pages
from .lets_plot_errors import check_lets_plot_message_errors

API_PAGES_DIR = "docs/python/pages/api"

@pytest.mark.parametrize(('page'), generate_pages(API_PAGES_DIR))
def test_api_example(page):
    with page_parser(page) as (parser, parser_type):
        check_lets_plot_message_errors(parser, parser_type, page, warn_only=False)

def test_api_list():
    API_EXPECTED_EXTRA = {
        "PlotSpec", "NamesGeocoder",
        "palette",
        "LETS_PLOT_COLOR", "LETS_PLOT_LIGHT", "LETS_PLOT_DARK", "LETS_PLOT_BW",
        "SOLID", "OSM", "OPEN_TOPO_MAP",
        "CARTO_POSITRON", "CARTO_POSITRON_HIRES", "CARTO_POSITRON_NO_LABELS", "CARTO_POSITRON_NO_LABELS_HIRES", "CARTO_DARK_MATTER_NO_LABELS", "CARTO_DARK_MATTER_NO_LABELS_HIRES", "CARTO_VOYAGER", "CARTO_VOYAGER_HIRES", "CARTO_MIDNIGHT_COMMANDER", "CARTO_MIDNIGHT_COMMANDER_HIRES", "CARTO_ANTIQUE", "CARTO_ANTIQUE_HIRES", "CARTO_FLAT_BLUE", "CARTO_FLAT_BLUE_HIRES",
        "NASA_CITYLIGHTS_2012", "NASA_BLUEMARBLE_NEXTGENERATION", "NASA_GREYSCALE_SHADED_RELIEF_30M", "NASA_COLOR_SHADED_RELIEF_30M", "NASA_TERRA_TRUECOLOR",
    }
    module_members = get_module_members()
    api_members = get_api_members()
    api_extra = api_members.difference(module_members).difference(API_EXPECTED_EXTRA)
    assert len(api_extra) == 0, "\nExtra API members:\n{0}".format(format_members(api_extra))
    forgotten_members = module_members.difference(api_members)
    if len(forgotten_members) > 0:
        warnings.warn(UserWarning("\nNon mentioned API members:\n{0}".format(format_members(forgotten_members))))

def get_module_members(module=lp):
    def get_submodule_members(submodule):
        if not hasattr(submodule, '__all__'):
            return set()
        return {name for name in submodule.__all__ if name[0] != "_"}
    members = set()
    members = members.union(get_submodule_members(module))
    for name, submodule in inspect.getmembers(module, inspect.ismodule):
        if name[0] == "_" or not "lets_plot" in submodule.__package__:
            continue
        members = members.union(get_module_members(submodule))
    return members

def get_api_members():
    members = []
    with open("docs/python/pages/api.html", 'r', encoding='utf-8') as page:
        soup = BeautifulSoup(page, 'html.parser')
        for a in soup.select("a.internal span.pre"):
            members.append(a.text.strip())
    duplicates = {k: v for k, v in val_counts(members).items() if v > 1}
    if any(duplicates):
        warnings.warn(UserWarning("\nThere is duplicates in API members:\n{0}".format(duplicates)))
    return set(members)

def val_counts(l):
    d = {}
    for v in l:
        if v in d.keys():
            d[v] += 1
        else:
            d[v] = 1
    return dict(sorted(d.items(), key=lambda it: it[1], reverse=True))

def format_members(members):
    members_list = ["  {0}".format(s) for s in members]
    members_list.sort()
    return "\n".join(members_list)