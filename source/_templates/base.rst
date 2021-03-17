{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

{% if objtype == 'class' %}
.. autoclass:: {{ objname }}
  :members:
  :special-members: __init__
{% else %}
.. auto{{ objtype }}:: {{ objname }}
{% endif %}