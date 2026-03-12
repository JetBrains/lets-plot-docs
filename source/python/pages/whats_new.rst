.. _whats_new:

.. title:: What is New


What Is New in 4.9.0
====================

- **Statistical Summaries Directly on geom_smooth() Plot Layer**

  The :py:func:`geom_smooth() <lets_plot.geom_smooth>` layer now includes a ``labels`` parameter designed to display statistical summaries of the fitted model directly on the plot.
  This parameter accepts a :py:func:`smooth_labels() <lets_plot.smooth_labels>` object, which provides access to model-specific variables like :math:`R^2` and the regression equation.

  .. image:: /_static/images/changelog/4.9.0/smooth_summary.png
    :width: 400
    :height: 265

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/smooth_summary.html>`__.

- **Plot Tags**

  Plot tags are short labels attached to a plot.

  .. image:: /_static/images/changelog/4.9.0/plot_tags.png
    :width: 600
    :height: 185

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/plot_tags.html>`__.

- **New geom_bracket() and geom_bracket_dodge() Geometries**

  New geometries designed primarily for significance bars (*p-values*) annotations in categorical plots.

  .. image:: /_static/images/changelog/4.9.0/geom_bracket.png
    :width: 400
    :height: 261

  See: `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/geom_bracket.html>`__.

- **Custom Color Palettes in geom_imshow()**

  The ``cmap`` parameter now allows you to specify a list of hex color codes for visualizing grayscale images.
  Also, the new ``cguide`` parameter lets you customize the colorbar for grayscale images.

  .. image:: /_static/images/changelog/4.9.0/image_custom_cmap.png
    :width: 400
    :height: 248

  See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/image_custom_cmap.html>`__.

- **New palette() Method in Color Scales**

  Generates a list of hex color codes that can be used with :py:func:`scale_color_manual() <lets_plot.scale_color_manual>` to maintain consistent colors across multiple plots.

  See: `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/scale_color_palette.html>`__.

- **New overflow parameter in scale_color_brewer(), scale_fill_brewer()**

  Controls how colors are generated when more colors are needed than the palette provides.
  Options: ``'interpolate'`` (``'i'``), ``'cycle'`` (``'c'``), ``'generate'`` (``'g'``).

  See: `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/scale_brewer_overflow.html>`__.

- **New break_width Parameter in Positional Scales**

  Specifies a fixed distance between axis breaks.

  See examples:

  - `datetime scale <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/scale_break_width_datetime.html>`__
  - `time (duration) scale <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/scale_break_width_duration.html>`__
  - `log10 scale <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/scale_break_width_log10.html>`__

- **Axis Minor Ticks Customization**

  The ``axis_minor_ticks`` and ``axis_minor_ticks_length`` parameters in :py:func:`theme() <lets_plot.theme>`.

  See: `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/axis_minor_ticks.html>`__.

- **Pan/Zoom in gggrid() with Shared Axes**

  Pan/Zoom now propagates across subplots with shared axes (``sharex``/``sharey``).

  See: `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26a/gggrid_scale_share_zoom.html>`__.

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
  :target: https://lets-plot.org/examples/demo/raincloud.html

.. image:: /_static/images/changelog/4.7.0/square-europe_capitals.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/europe_capitals.html

.. image:: /_static/images/changelog/4.7.0/square-trading_chart.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/trading_chart.html

.. image:: /_static/images/changelog/4.6.0/square-magnifier_inset.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/magnifier_inset.html

.. raw:: html

    <br/>

.. image:: /_static/images/changelog/4.6.0/square-ggbunch_indonesia.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/ggbunch_indonesia.html

.. image:: /_static/images/changelog/4.7.0/square-lets_plot_in_2024.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/lets_plot_in_2024.html

.. image:: /_static/images/changelog/4.7.0/square-plot_layout_scheme.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/plot_layout_scheme.html

.. image:: /_static/images/changelog/4.5.0/legend_theme.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/theme_legend_scheme.html


Changelog
---------

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.