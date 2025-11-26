:og:description: {{ (fullname | shortdesc) or (name ~ ' in Lets-Plot Python API.') | escape }}

.. title:: {{ name }}{% if objtype in ('function', 'method') %}(){% endif %} | Lets-Plot Python API

.. meta::
   :description: {{ (fullname | shortdesc) or (name ~ ' in Lets-Plot Python API.') | escape }}

{{ name | escape | underline}}

.. currentmodule:: {{ module }}

{% if objtype == 'class' %}
.. autoclass:: {{ objname }}
  :members:
  :special-members: __init__, __add__
  :inherited-members:
{% else %}
.. auto{{ objtype }}:: {{ objname }}
{% endif %}