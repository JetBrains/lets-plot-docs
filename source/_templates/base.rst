{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. auto{{ objtype }}:: {{ objname }}

{% if classes %}
  {% block classes %}
    .. rubric:: Classes
    .. autosummary::
       :toctree: .
       :template: base.rst
       :recursive:
       {% for class in classes %}
         {{ class }}
       {% endfor %}
  {% endblock %}
{% endif %}

{% if functions %}
  {% block functions %}
    .. rubric:: Functions
    .. autosummary::
       :toctree: .
       :template: base.rst
       :recursive:
       {% for function in functions %}
         {%- if not function.startswith('_') %}
           {{ function }}
         {%- endif -%}
       {% endfor %}
  {% endblock %}
{% endif %}

{% if methods %}
  {% block methods %}
    .. rubric:: Methods
    .. autosummary::
       :toctree: .
       :template: base.rst
       :recursive:
       {% for method in methods %}
         {%- if not method.startswith('_') %}
           ~{{ name }}.{{ method }}
         {%- endif -%}
       {%- endfor %}
  {% endblock %}
{% endif %}

{% if attributes %}
  {% block attributes %}
    .. rubric:: Attributes
    .. autosummary::
       {% for attribute in attributes %}
         {%- if not attribute.startswith('_') %}
           ~{{ name }}.{{ attribute }}
         {%- endif -%}
       {%- endfor %}
  {% endblock %}
{% endif %}