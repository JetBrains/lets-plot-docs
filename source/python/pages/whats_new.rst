.. _whats_new:

.. title:: What is New


What is new in 4.3.0
====================

- **coord_polar()**

  The polar coordinate system is most commonly used for pie charts, but it can also be used for constructing **Spyder or Radar charts** using the ``flat`` option.

  .. image:: /_static/images/changelog/4.3.0/polar_coord_pie.png
    :width: 256

  .. image:: /_static/images/changelog/4.3.0/radar_chart.png
    :width: 256

  See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-24a/coord_polar.ipynb>`__.

- **In the theme()**

  - ``panel_inset`` parameter - primarily used for plots with polar coordinates.

    See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-24a/theme_panel_inset.ipynb>`__.

  - ``panel_border_ontop`` parameter - enables the drawing of panel border on top of the plot geoms.

  - ``panel_grid_ontop``, ``panel_grid_ontop_x``, ``panel_grid_ontop_y`` parameters - enable the drawing of grid lines on top of the plot geoms.

- **geom_curve()**

  .. image:: /_static/images/changelog/4.3.0/curve_annotation.png
    :width: 338

  See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-24a/geom_curve.ipynb>`__.

- **[UNIQUE] Visualizing Graph-like Data with geom_segment() and geom_curve()**

  - Aesthetics ``size_start``, ``size_end``, ``stroke_start`` and ``stroke_end`` enable better alignment of segments/curves with nodes of the graph by considering the size of the nodes.

  - The ``spacer`` parameter allows for additional manual fine-tuning.

  .. image:: /_static/images/changelog/4.3.0/graph_simple.png
    :width: 256

  .. image:: /_static/images/changelog/4.3.0/graph_on_map.png
    :width: 256

  See:

  - `A simple graph example <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-24a/graph_edges.ipynb>`__

  - `An interactive map example <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-24a/geom_curve_on_map.ipynb>`__

- **The alpha_stroke Parameter in geom_label()**

  Use the ``alpha_stroke`` parameter to apply ``alpha`` to entire ``label``. By default, ``alpha`` is only applied to the label background.

  See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-24a/geom_label_alpha_stroke.ipynb>`__.

- **Showing Plots in External Browser**

  The :py:meth:`LetsPlot.setup_show_ext() <lets_plot.LetsPlot.setup_show_ext>` directive allows plots to be displayed in an external browser window.

Recent Updates in the Gallery
-----------------------------

.. image:: /_static/images/changelog/4.3.3/sunshine_hours.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/sunshine_hours.ipynb

.. image:: /_static/images/changelog/4.3.2/30_day_chart_2.png
  :width: 128
  :height: 128
  :target: https://www.ddanieltan.com/posts/30-day-chart-2/index.html

.. image:: /_static/images/changelog/4.3.2/mpg_corrgram.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/mpg_corrgram.ipynb

.. image:: /_static/images/changelog/4.3.1/gal_venn_diagram.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/venn_diagram.ipynb

.. image:: /_static/images/changelog/4.3.1/gal_spoke.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/cookbook/geom_spoke.ipynb

.. image:: /_static/images/changelog/4.3.1/gal_indonesia_volcanoes_on_map.png
  :width: 128
  :height: 128
  :target: https://www.kaggle.com/code/alshan/indonesia-volcanoes-on-map

.. raw:: html

    <br/>

.. image:: /_static/images/changelog/4.3.1/gal_japanese_volcanoes_on_map.png
  :width: 128
  :height: 128
  :target: https://www.kaggle.com/code/alshan/japanese-volcanoes-on-map

.. image:: /_static/images/changelog/4.3.0/gal_bbc_cookbook.png
  :width: 128
  :height: 128
  :target: https://nextjournal.com/asmirnov-horis/bbc-visual-and-data-journalism-cookbook-for-lets-plot

.. image:: /_static/images/changelog/4.3.0/gal_penguins.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/palmer_penguins.ipynb

.. image:: /_static/images/changelog/4.3.0/gal_periodic_table.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/periodic_table.ipynb

.. image:: /_static/images/changelog/4.3.0/gal_wind_rose.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/wind_rose.ipynb

.. image:: /_static/images/changelog/4.3.0/gal_polar_heatmap.png
  :width: 128
  :height: 128
  :target: https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/demo/heatmap_in_polar_coord.ipynb


Change Log
----------

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.