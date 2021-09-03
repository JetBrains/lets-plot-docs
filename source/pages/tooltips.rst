.. _tooltips:

Tooltip Customization
#####################

- :ref:`Tooltip variable list <tooltips_variables>`
- :ref:`Formatting tooltip fields <tooltips_formatting>`
- :ref:`Customizing tooltip lines <tooltips_lines>`

  - :ref:`Labels configuration <tooltips_labels_configuration>`

- :ref:`Tooltip anchor <tooltips_anchor>`
- :ref:`Minimum width of a general tooltip <tooltips_minwidth>`
- :ref:`Tooltip color <tooltips_color>`
- :ref:`Examples <tooltips_examples>`
- :ref:`Outlier tooltips configuration <tooltips_outliers>`

  - :ref:`Examples <tooltips_example_outliers>`

- :ref:`Hiding tooltips <tooltips_hiding_tooltips>`
- :ref:`Example Notebooks <tooltips_example_notebooks>`
    
----

You can customize the content of tooltips for the layer by using the parameter ``tooltips`` of ``geom`` functions.

The following functions set lines, define formatting of the tooltip, its location and width:

.. code-block:: python

    tooltips=layer_tooltips(variables)
        .format(field, format)
        .line(template)
        .anchor(position)
        .min_width(value)


.. _tooltips_variables:

Tooltip variable list: ``layer_tooltips(variables=['var_name_1', ..., 'var_name_N'])``
======================================================================================

The ``variables`` parameter defines a list of variable names, which values will be placed line by line in the general tooltip.
If formatting is specified for a variable from this list (with the ``format()`` function), it will be applied.
Otherwise, the default formatting is used.
Additional tooltip lines can be specified using the ``line()`` functions.


.. _tooltips_formatting:

Formatting tooltip fields: ``layer_tooltips().format(field, format)``
=====================================================================

Defines the format for displaying the value.
The format will be applied to the mapped value in the default tooltip or to the corresponding value specified in the ``line`` template.

Arguments
---------

- ``field`` (string): The name of the variable/aesthetics. The field name begins with ``^`` for aesthetics. You can specify variable names without a prefix, but the ``@`` prefix can be also used. It's possible to set a format for all positional aesthetics: ``^X`` (all positional x) and ``^Y`` (all positional y). For example:

  - ``field = '^Y'`` - for all positional y;
  - ``field = '^y'`` - for y aesthetic;
  - ``field = 'y'`` - for variable with the name "y".

- ``format`` (string): The format to apply to the field. The format contains a number format (``'1.f'``) or a string template (``'{.1f}'``). The numeric format for non-numeric value will be ignored. The string template contains "replacement fields" surrounded by curly braces ``{}``. Any code that is not in the braces is considered literal text, and it will be copied unchanged to the result string. If you need to include a brace character into the literal text, it can be escaped by doubling: {{ and }}. For example:

  - ``.format('^color', '.1f')`` -> ``"17.0"``;
  - ``.format('cty', '{.2f} (mpg)'))`` -> ``"17.00 (mpg)"``;
  - ``.format('^color', '{{{.2f}}}')`` -> ``"{17.00}"``;
  - ``.format('model', '{} {{text}}')`` -> ``"mustang {text}"``.

The string template in the ``format`` parameter will allow changing lines for the default tooltip without ``line`` specifying.

Variable's and aesthetic's formats are not interchangeable, for example, ``var`` format will not be applied to ``aes`` mapped to this variable.


.. _tooltips_lines:

Customizing tooltip lines: ``layer_tooltips().line(template)``
==============================================================

Specifies the string template to use in a general tooltip. If you add ``line()``, it overrides the default tooltip.

Variables and aesthetics can be accessed via a special syntax:

- ``^color`` for aesthetic;
- ``@year`` for variable;
- ``@{number of cylinders}`` for a variable with spaces or non-word characters in the name;
- ``@..count..`` for statistics variables.

A '^' symbol can be escaped with a backslash; a brace character in the literal text - by doubling:

- ``.line('text')`` -> ``"text"``;
- ``.line('\^text')`` -> ``"^text"``;
- ``.line('{{text}}')`` -> ``"{text}"``;
- ``.line('@model')`` -> ``"mustang"``;
- ``.line('{{@model}}')`` -> ``"{mustang}"``.


.. _tooltips_labels_configuration:

Labels configuration
--------------------

The default tooltip has a label before the value usually containing the name of the mapped variable.
It has its own behaviour similar to a blank label for an axis aesthetics. 
This default label can be set in the template by using a pair of symbols ``@|``.
You can override the label by specifying a string value before ``|`` symbol.

Within the tooltip line, ou can align a label to left. The string formed by a template can be aligned to right.
If you do not specify a label, the string will be centered in the tooltip. For example:

- ``line('^color')``: no label, value is centered;
- ``line('|^color')``: label is empty, value is right-aligned;
- ``line('@|^color')``: default label is used, value is right-aligned;
- ``line('my label|^color')``: label is specified, value is right-aligned.


.. _tooltips_anchor:

Tooltip anchor: ``layer_tooltips().anchor(position)``
=====================================================

Specifies a fixed position for a general tooltip.

The ``anchor()`` function accepts the following values:

- 'top_right'
- 'top_center'
- 'top_left' 
- 'bottom_right' 
- 'bottom_center'
- 'bottom_left'
- 'middle_right'
- 'middle_center' 
- 'middle_left'


.. _tooltips_minwidth:

Minimum width of a general tooltip: ``layer_tooltips().min_width(value)``
=========================================================================

Specifies a minimum width of a general tooltip in pixels.


.. _tooltips_color:

Tooltip color: ``layer_tooltips().color(value)``
================================================

Specifies a color of a general tooltip.


.. _tooltips_examples:

Examples
========

.. jupyter-execute::
    :linenos:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df) + geom_point(aes(x='displ', y='cty', fill='drv', size='hwy'), shape=21, color='black', \
                            tooltips=layer_tooltips().format('cty', '.1f')
                                                     .format('hwy', '.1f')
                                                     .format('drv', '{}wd')
                                                     .line('@manufacturer @model')
                                                     .line('cty/hwy|@cty/@hwy')
                                                     .line('@|@class')
                                                     .line('drive train|@drv')
                                                     .line('@|@year'))

Change format for the default tooltip:

.. jupyter-execute::
    :linenos:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df) + geom_point(aes(x='displ', y='cty', fill='drv', size='hwy'), shape=21, color='black', \
                            tooltips=layer_tooltips().format('^fill', '{.2f} (mpg)'))

Set list of variables to place them in a multiline tooltip with the default formatting:

.. jupyter-execute::
    :linenos:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df) + geom_point(aes(x='displ', y='cty', fill='drv', size='hwy'), shape=21, color='black',
                            tooltips=layer_tooltips(['manufacturer', 'model', 'class', 'drv']))

Define the format for the variable from the list and specify an additional line:

.. jupyter-execute::
    :linenos:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df) + geom_point(aes(x='displ', y='cty', fill='drv', size='hwy'), shape=21, color='black',
                            tooltips=layer_tooltips(['manufacturer', 'model', 'class', 'drv'])
                                          .format('drv', '{}wd')
                                          .line('cty/hwy [mpg]|@cty/@hwy'))

Place a general tooltip at the top center and define its minimum width:

.. jupyter-execute::
    :linenos:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df) + geom_point(aes(x='displ', y='cty', fill='drv', size='hwy'), shape=21, color='black', \
                            tooltips=layer_tooltips().format('cty', '.1f')
                                                     .format('hwy', '.1f')
                                                     .format('drv', '{}wd')
                                                     .line('@manufacturer @model')
                                                     .line('cty/hwy|@cty/@hwy')
                                                     .line('@|@class')
                                                     .line('drive train|@drv')
                                                     .line('@|@year')
                                                     .anchor('top_center')
                                                     .min_width(200))


Move the tooltips to the top right corner:

.. jupyter-execute::
    :linenos:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df) + geom_point(aes(x='displ', y='cty', fill='drv', size='hwy'), shape=21, color='black', \
                            tooltips=layer_tooltips().anchor('top_right').format('^fill', '{.2f} (mpg)'))


.. _tooltips_outliers:

Outlier tooltips configuration
==============================

The default an outlier's tooltip contains a string like ``'name: value'``: there is no label and no alignment.
It's possible to change formatting of it with the ``format`` function. The number format (``'1.f'``) leaves 
the string as is (``'name: value'``) and formats the value. The string template replaces the default string:
``‘{.1f}`` - with ``'value'``, ``'format text {.1f}'`` - with ``"format text value"``.

The specified ``line`` for an outlier will move it to a general multi-line tooltip.


.. _tooltips_example_outliers:

Examples
--------

Change formatting for outliers:

.. jupyter-execute::
    :linenos:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df, aes('class', 'hwy')) + \
        geom_boxplot(tooltips=layer_tooltips().format('^Y', '.2f')        # all positionals
                                              .format('^ymax', '.3f')     # use number format --> "ymax: value"
                                              .format('^middle', '{.3f}') # use line format --> "value"
                                              .format('^ymin', 'ymin is {.3f}')) + \
        theme(legend_position='none')

Move outliers to a general tooltip:

.. jupyter-execute::
    :linenos:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df, aes('class', 'hwy')) + \
        geom_boxplot(tooltips=layer_tooltips().line('lower/upper|^lower, ^upper')) + \
        theme(legend_position='none')

Place tooltip at the top center and change its color:

.. jupyter-execute::
    :linenos:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df, aes('class', 'hwy')) + \
        geom_boxplot(tooltips=layer_tooltips().anchor('top_center')
                                              .color('cyan')
                                              .format('^Y', '.0f')
                                              .format('^middle', '.2f')
                                              .line('@|^middle')
                                              .line('lower/upper|^lower/^upper')
                                              .line('min/max|^ymin/^ymax')) + \
        theme(legend_position='none')


.. _tooltips_hiding_tooltips:

Hiding tooltips
===============

Set ``tooltips = "none"`` to hide tooltips from the layer.


.. _tooltips_example_notebooks:

Example Notebooks
=================
 
- `tooltip_config.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/tooltip_config.ipynb>`_

- Visualization of Airport Data on Map: |airport_data_kaggle|

.. |airport_data_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/alshan/visualization-of-airport-data-on-map