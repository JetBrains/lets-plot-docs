.. _whats_new:

.. title:: What is New


What Is New in 4.7.0
====================

- **Time Series Plotting**

  - Support for Python ``time`` and ``date`` objects.

  - Support for timezone-aware ``datetime`` objects and Pandas/Polars ``Series``.

  .. image:: /_static/images/changelog/4.7.0/time_date_datetime.png
    :width: 400
    :height: 237

  See `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-25b/time_date_datetime.ipynb>`__.

- **Native Support for PNG and PDF Exports**

  Exporting to PNG and PDF formats now uses the ``ImageMagick`` library bundled with Lets-Plot Python wheels and available out-of-the-box.

  This replaces the previous dependency on the ``CairoSVG`` library and comes with improved support for LaTeX labels rasterization.

- **geom_sina() Geometry**

  .. image:: /_static/images/changelog/4.7.0/geom_sina.png
    :width: 400
    :height: 276

  See `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-25b/geom_sina.ipynb>`__.

- **geom_text_repel() and geom_label_repel() Geometries**

  .. image:: /_static/images/changelog/4.7.0/geom_repel.png
    :width: 400
    :height: 232

  See `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-25b/ggrepel.ipynb>`__.

- **waterfall_plot() Chart**

  - Annotations support via ``relative_labels`` and ``absolute_labels`` parameters.

    .. image:: /_static/images/changelog/4.7.0/waterfall_plot_annotations.png
      :width: 400
      :height: 253

    See `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-25b/waterfall_plot_annotations.ipynb>`__.

  - Support for combining waterfall bars with other geometry layers.

    .. image:: /_static/images/changelog/4.7.0/waterfall_plot_layers.png
      :width: 400
      :height: 227

    See `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-25b/waterfall_plot_layers.ipynb>`__.

- **Continuous Data on Discrete Scales**

  Continuous data when used with discrete positional scales is no longer transformed to discrete data. Instead, it remains continuous, allowing for precise positioning of continuous elements relative to discrete ones.

  .. image:: /_static/images/changelog/4.7.0/combo_discrete_continuous.png
    :width: 400
    :height: 151

  See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-25b/numeric_data_on_discrete_scale.ipynb>`__.

.. tip::

   New way of handling continuous data on discrete scales could potentially break existing plots. If you want to restore a broken plot to its original form, you can use the :py:mod:`as_discrete() <lets_plot.mapping.as_discrete>` function to annotate continuous data as discrete.

- **Plot Layout**

  The default plot layout has been improved to better accommodate axis labels and titles.
  Also, new ``theme()`` options ``axis_text_spacing``, ``axis_text_spacing_x``, and ``axis_text_spacing_y`` control spacing between axis ticks and labels.

  .. image:: /_static/images/changelog/4.7.0/plot_layout_diagram.png
    :width: 400
    :height: 175

  See the `plot layout diagram <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-25b/plot_layout_scheme.ipynb>`__ showing various layout options and their effects on plot appearance.

- **And More**

  See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for a full list of changes.


Recent Updates in the :doc:`Gallery </python/pages/gallery>`
------------------------------------------------------------

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