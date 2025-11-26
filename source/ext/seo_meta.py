#
# Copyright (c) 2025. JetBrains s.r.o.
# Use of this source code is governed by the MIT license that can be found in the LICENSE file.
#

import re
import inspect
import textwrap
from pydoc import locate
from jinja2.defaults import DEFAULT_FILTERS


def shortdesc(fullname):
    obj = locate(fullname)
    if obj is None:
        return ""
    doc = inspect.getdoc(obj) or ""
    if not doc:
        return ""
    doc = textwrap.dedent(doc).strip()                    # Normalize indentation and strip leading/trailing spaces
    doc = doc.split("\n\n", 1)[0]                         # First paragraph
    doc = " ".join(doc.split())                           # Collapse whitespace
    # --- Clean basic reST inline markup ---
    doc = re.sub(r"``([^`]*)``", r"\1", doc)              # ``code`` -> code
    doc = re.sub(r"`([^`<]+)\s+<[^>]+>`__?", r"\1", doc)  # `Text <url>`__, `Text <url>`_ -> Text
    doc = re.sub(r"`([^`]+)`_", r"\1", doc)               # `ref`_ -> ref
    doc = re.sub(r":\w+:`([^`]+)`", r"\1", doc)           # :role:`text` -> text
    # --- Keep only the first sentence ---
    doc = re.split(r'(?<=[.!?])\s', doc, 1)[0]            # Split on first sentence-ending punctuation followed by whitespace
    # --- Special cases ---
    # Signature dump of the tilesets
    if doc.startswith("dict() -> new empty dictionary"):
        return ""
    return doc


DEFAULT_FILTERS["shortdesc"] = shortdesc


def setup(app):
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }