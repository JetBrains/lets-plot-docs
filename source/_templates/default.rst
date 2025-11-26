:og:description: {{ (fullname | shortdesc) or (name ~ ' in Lets-Plot Python API.') | escape }}

.. title:: {{ name }}{% if objtype in ('function', 'method') %}(){% endif %} | Lets-Plot Python API

.. meta::
   :description: {{ (fullname | shortdesc) or (name ~ ' in Lets-Plot Python API.') | escape }}

{{ name | escape | underline}}

.. currentmodule:: {{ module }}

.. auto{{ objtype }}:: {{ objname }}