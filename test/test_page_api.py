#!/usr/bin/env python

import inspect
import codecs
import warnings

from bs4 import BeautifulSoup

import lets_plot as lp
from lets_plot.bistro.corr import *
from lets_plot.geo_data import *

def test_page_api():
    API_EXPECTED_EXTRA = {
        "FeatureSpec", "PlotSpec", "LayerSpec", "NamesGeocoder", "ReverseGeocoder",
        "as_discrete",
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
    members = set()
    with codecs.open("docs/pages/api.html", 'r', 'utf-8') as page:
        soup = BeautifulSoup(page, 'html.parser')
        for a in soup.select("a.internal span.pre"):
            members.add(a.text.strip())
    return members

def format_members(members):
    members_list = ["  {0}".format(s) for s in members]
    members_list.sort()
    return "\n".join(members_list)