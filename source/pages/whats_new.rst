.. _whats_new:

.. title:: What is new


What is new in 4.2.0
====================

- **Support for "Categoricals"**

  See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/factor_levels.ipynb>`__.

- **Superscript for Numbers in Scientific Notation**

  .. warning::
    Do NOT(!) use ``exponent_format='pow'`` if you are planning to export plot to a raster format (PNG, PDF).

    The ``CairoSVG`` library (which is under the hood of our ``ggsave()`` function) does not handle ``tspan`` element properly end breaks superscript notation when transforming SVG to PNG/PDF.

    More details: https://github.com/Kozea/CairoSVG/issues/317

  .. image:: /_static/images/changelog/4.2.0/superscript.png
    :width: 328

  See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/superscript_exponent.ipynb>`__.

- **Exporting Plot to a File-Like Object**

  Convenience methods: ``to_svg()``, ``to_html()``, ``to_png()``, ``to_pdf()``

  See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/new_export_methods.ipynb>`__.

- **Sharing of X,Y-scale Limits Between Subplots in gggrid()**

  See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/gggrid_scale_share.ipynb>`__.

- **geom_spoke()**

  .. image:: /_static/images/changelog/4.2.0/geom_spoke.png
    :width: 248

  See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/geom_spoke.ipynb>`__.

- **High-contrast Tileset "BW" for geom_livemap()**

  .. image:: /_static/images/changelog/4.2.0/tileset_BW.png
    :width: 512

  See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/geom_livemap_bw_tiles.ipynb>`__.

  See advanced example: `Spatial prediction of soil pollutants with multi-output Gaussian processes <https://nextjournal.com/asmirnov-horis/spatial-prediction-of-soil-pollutants-with-multi-output-gaussian-processes?token=26GT2sBa3Ycw6LGZxqdTay>`__. Credits: Essi Parent (`@essicolo <https://github.com/essicolo>`__).

- **Other New Features and Improvements**

  - :py:mod:`scale_x_log2() <lets_plot.scale_x_log2>`, :py:mod:`scale_y_log2() <lets_plot.scale_y_log2>`

  - New variables computed by ``'count'`` and ``'count2d'`` statistics: ``'..sumprop..'``, ``'..sumpct..'``.

    See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/new_stat_count_vars.ipynb>`__.

  - Support using dictionaries for breaks/labels/values customization in ``scale_xxx()`` functions.

    See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/scale_params_with_dict.ipynb>`__.

  - The ``lablim`` parameter in ``scale_xxx()`` functions.

    See: `example notebook <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/scale_lablim.ipynb>`__.

  - ``label_text`` parameter in :py:mod:`theme() <lets_plot.theme>` for annotation text settings.

    See: `example notebook <https://nbviewer.org/github/JetBrains/lets-plot/blob/master/docs/f-23f/theme_label_text.ipynb>`__.

  - NumberFormat: new flag ``~`` to trim trailing zeros.


Change Log
----------

See `CHANGELOG.md <https://github.com/JetBrains/lets-plot/blob/master/CHANGELOG.md>`__ for other changes and fixes.