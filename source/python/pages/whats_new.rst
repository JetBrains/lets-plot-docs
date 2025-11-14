.. _whats_new:

.. title:: What is New


What Is New in 4.8.0
====================

- **geom_pointdensity() Geometry**

  .. image:: /_static/images/changelog/4.8.0/geom_pointdensity.png
    :width: 400
    :height: 246

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-25e/geom_pointdensity.html>`__.

- **Explicit group aesthetic now overrides default grouping behavior instead of combining with it**

  .. important::

    **BREAKING CHANGE:**

    Previously, setting ``group='variable'`` would group by both the
    explicit variable AND any discrete aesthetics (color, shape, etc.).
    Now it groups ONLY by the explicit variable, matching ``ggplot2``
    behavior.
    Use ``group=[var1, var2, ...]`` to group by multiple variables
    explicitly,
    and ``group=[]`` to disable any grouping.

  .. image:: /_static/images/changelog/4.8.0/group_override_defaults.png
    :width: 400
    :height: 263

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-25e/group_override_defaults.html>`__.

- **gggrid(): support for shared legends (parameter guides)**

  .. image:: /_static/images/changelog/4.8.0/gggrid_legend_collect.png
    :width: 500
    :height: 172

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-25e/gggrid_legend_collect.html>`__.

- **Better handling of missing values in geom_line(), geom_path(), geom_ribbon(), and geom_area()**

  .. image:: /_static/images/changelog/4.8.0/missing_values_ribbon.png
    :width: 500
    :height: 192

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-25e/missing_values_line_path_area_ribbon.html>`__.

- **geom_histogram(): custom bin bounds (parameter breaks)**

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-25e/geom_histogram_param_breaks.html>`__.

- **Legend automatically wraps to prevent overlap — up to 15 rows for vertical legends and 5 columns for horizontal ones**

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-25e/legend_wrap.html>`__.

- **flavor_standard() resets the theme’s default color scheme**

  Use to override other flavors or make defaults explicit.

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-25e/flavor_standard.html>`__.

- **'left', 'right', 'top', and 'bottom' legend justification**

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-25e/legend_justification.html>`__.

- **ggtb(): Added size_zoomin and size_basis parameters to control point size scaling behavior when zooming (works with geom_point and related layers)**

  See: `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-25e/ggtb_size_zoomin.html>`__.

- **And More**

  See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for a full list of changes.


Recent Updates in the :doc:`Gallery </python/pages/gallery>`
------------------------------------------------------------

.. image:: /_static/images/changelog/4.8.0/square-cities_density.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/cities_density.html

.. image:: /_static/images/changelog/4.7.0/square-raincloud.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/raincloud.ipynb

.. image:: /_static/images/changelog/4.7.0/square-europe_capitals.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/europe_capitals.ipynb

.. image:: /_static/images/changelog/4.7.0/square-trading_chart.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/trading_chart.ipynb

.. image:: /_static/images/changelog/4.6.0/square-magnifier_inset.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/magnifier_inset.ipynb

.. raw:: html

    <br/>

.. image:: /_static/images/changelog/4.6.0/square-ggbunch_indonesia.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/ggbunch_indonesia.ipynb

.. image:: /_static/images/changelog/4.7.0/square-lets_plot_in_2024.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/lets_plot_in_2024.ipynb

.. image:: /_static/images/changelog/4.7.0/square-plot_layout_scheme.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/plot_layout_scheme.ipynb

.. image:: /_static/images/changelog/4.5.0/legend_theme.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/theme_legend_scheme.ipynb


Change Log
----------

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.