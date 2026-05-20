.. _whats_new:

.. title:: What is New


What Is New in 4.10.0
=====================

- **ggdeck()**

  The new :py:func:`ggdeck() <lets_plot.ggdeck>` function overlays multiple independent plots in a
  shared plotting area. Typically, all plots share one axis — enabling dual-axis charts and multivariate comparisons.

  - **Dual Axis:**

    .. image:: /_static/images/changelog/4.10.0/ggdeck_dual_axis.png
      :width: 550
      :height: 295

    See: `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26b/ggdeck_dual_axis.html>`__.

  - **Multivariate Comparison:**

    .. image:: /_static/images/changelog/4.10.0/ggdeck_plot_overlay.png
      :width: 600
      :height: 283

    See `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26b/ggdeck_plot_overlay.html>`__.

- **Alpha Channel in Color Strings**

  - Named colors accept an opacity suffix after a slash: ``"steelblue/0.35"``.
  - Hex colors accept an alpha channel: ``#RRGGBBAA`` or short form ``#RGBA``.

  .. image:: /_static/images/changelog/4.10.0/color_alpha_componnet.png
    :width: 400
    :height: 214

  See: `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26b/color_alpha.html>`__.

- **Text Angle in Facet Strip Labels**

  Facet strip labels can now be rotated via the ``angle`` parameter of
  :py:func:`element_text() <lets_plot.element_text>`, applied to ``strip_text``, ``strip_text_x``, or
  ``strip_text_y``.

  Thanks to a contribution by `tentrillion <https://github.com/tentrillion>`__.

  .. image:: /_static/images/changelog/4.10.0/facet_strip_text_angle.png
    :width: 400
    :height: 225

  See: `example notebook <https://raw.githack.com/JetBrains/lets-plot/master/docs/f-26b/strip_text_angle.html>`__.

- **And More**

  See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for a full list of changes.


Recent Updates in the :doc:`Gallery </python/pages/gallery>`
------------------------------------------------------------

.. image:: /_static/images/changelog/4.10.0/square-math_manual_legend.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/math_manual_legend.html

.. image:: /_static/images/changelog/4.10.0/square-earthquakes_in_2025.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/earthquakes_in_2025.html

.. image:: /_static/images/changelog/4.8.0/square-cities_density.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/cities_density.html

.. image:: /_static/images/changelog/4.7.0/square-raincloud.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/raincloud.html

.. raw:: html

    <br/>

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

.. image:: /_static/images/changelog/4.6.0/square-ggbunch_indonesia.png
  :width: 128
  :height: 128
  :target: https://lets-plot.org/examples/demo/ggbunch_indonesia.html

.. raw:: html

    <br/>

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