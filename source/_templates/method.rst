{% set dispname = (name.split('.') | last) %}

:og:description: {{ (fullname | shortdesc) or (dispname ~ ' in Lets-Plot Python API.') | escape }}

.. title:: {{ dispname }}() | Lets-Plot Python API

.. meta::
   :description: {{ (fullname | shortdesc) or (dispname ~ ' in Lets-Plot Python API.') | escape }}

{{ dispname | escape | underline}}

.. currentmodule:: {{ module }}

.. auto{{ objtype }}:: {{ objname }}