{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

{% if objtype == 'class' %}
.. autoclass:: {{ objname }}
  :members:
  :special-members: __init__
  :inherited-members:
{% else %}
.. auto{{ objtype }}:: {{ objname }}
{% endif %}