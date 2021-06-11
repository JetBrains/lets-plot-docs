.. _examples:

Example Notebooks
-----------------

Try the following tutorials and examples to learn and evaluate various
features of the ``Lets-Plot`` library.

- :ref:`Quickstart and User Guide <examples_quickstart>`
- :ref:`Geoms and Stats <examples_geoms_and_stats>`
- :ref:`Position Adjustment <examples_position>`
- :ref:`Scales <examples_scales>`
- :ref:`Facets <examples_facets>`
- :ref:`GGBunch <examples_ggbunch>`
- :ref:`as_discrete() function <examples_as_discrete>`
- :ref:`Export to File <examples_export>`
- :ref:`Formatting <examples_formatting>`
- :ref:`Theme <examples_theme>`
- :ref:`Data Sampling <examples_sampling>`
- :ref:`Tooltip Customization <examples_tooltips>`
- :ref:`The 'bistro' Package <examples_bistro>`
- :ref:`GeoPandas Support <examples_geopandas>`
- :ref:`Interactive Maps <examples_interactive_maps>`
- :ref:`Geocoding <examples_geocoding>`
- :ref:`Miscellaneous <examples_miscellaneous>`


.. _examples_quickstart:

Quickstart and User Guide
^^^^^^^^^^^^^^^^^^^^^^^^^

- Quickstart: |quickstart_nbviewer| |quickstart_datalore| |quickstart_kaggle| |quickstart_colab| |quickstart_deepnote|

.. |quickstart_nbviewer| image:: https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.png
    :width: 109px
    :height: 20px
    :target: https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/quickstart.ipynb
.. |quickstart_datalore| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg
    :width: 20px
    :height: 20px
    :alt: View in Datalore
    :target: https://view.datalore.io/notebook/Zzg9EVS6i16ELQo3arzWsP
.. |quickstart_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/alshan/lets-plot-quickstart
.. |quickstart_colab| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_colab.svg
    :width: 20px
    :height: 20px
    :alt: View at Colab
    :target: https://colab.research.google.com/drive/1uYYZcG0g0kP4lJdPkpWB8aBS96ioDii2?usp=sharing
.. |quickstart_deepnote| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_deepnote.svg
    :width: 20px
    :height: 20px
    :alt: View at Deepnote
    :target: https://deepnote.com/project/673ea421-638e-469d-8d04-5cc4c6e0258f#%2Fnotebook.ipynb

- `user_guide.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/guide/user_guide.ipynb>`__


.. _examples_geoms_and_stats:

Geoms and Stats
^^^^^^^^^^^^^^^

``geom_histogram()``, ``geom_density()``, ``geom_vline()``, ``geom_freqpoly()``, ``geom_boxplot()``:

`distributions.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/distributions.ipynb>`__

``geom_errorbar()``, ``geom_line()``, ``geom_point()``, ``geom_bar()``, ``geom_crossbar()``, ``geom_linerange()``, ``geom_pointrange()``:

`error_bars.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/error_bars.ipynb>`__

``geom_point()``, ``geom_smooth()`` (stat_smooth):

`scatter_plot.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/scatter_plot.ipynb>`__

`geom_smooth.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geom_smooth.ipynb>`__

``geom_density2d()``, ``geom_density2df()``, ``geom_bin2d()``, ``geom_polygon()``, ``geom_point()``:

`density_2d.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/density_2d.ipynb>`__

``geom_tile()``, ``geom_contour()``, ``geom_polygon()`` (Stat.contour), ``geom_contourf()``:

`contours.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/contours.ipynb>`__

``geom_image()``, ``geom_raster()``

``geom_image()``: displays an image specified by a ndarray with shape (n, m) or (n, m, 3) or (n, m, 4).

- `image_101.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_101.ipynb>`__
- `image_fisher_boat.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_fisher_boat.ipynb>`__

See also: ``image_matrix()`` in :ref:`The 'bistro' Package <examples_bistro>`.

``geom_text()``, label format

`label_format.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/label_format.ipynb>`__

``stat_corr()``

See the ``corr_plot()`` example in :ref:`The 'bistro' Package <examples_bistro>`.


.. _examples_position:

Position Adjustment
^^^^^^^^^^^^^^^^^^^

- ``position_dodge()``: `error_bars.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/error_bars.ipynb>`__
- ``position_jitter()``: `scatter_plot.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/scatter_plot.ipynb>`__


.. _examples_scales:

Scales
^^^^^^

- ``scale_color_manual()``, ``scale_fill_manual()``: `error_bars.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/error_bars.ipynb>`__
- ``scale_x_continuous()``, ``scale_shape_manual()``: `scatter_plot.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/scatter_plot.ipynb>`__
- ``scale_color_gradient()``: `density_2d.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/density_2d.ipynb>`__
- ``scale_fill_hue()``, ``scale_fill_grey()``, ``scale_color_gradient()``: `contours.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/contours.ipynb>`__


.. _examples_facets:

Facets
^^^^^^

- ``facet_grid()``, ``facet_wrap()``: `facets.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/facets.ipynb>`__


.. _examples_ggbunch:

GGBunch
^^^^^^^

GGBunch allows to show a collection of plots on one figure.
Each plot in the collection can have arbitrary location and size.
There is no automatic layout inside the bunch.

- `ggbunch.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/ggbunch.ipynb>`__
- `geom_smooth.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geom_smooth.ipynb>`__
- `scatter_matrix.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/scatter_matrix.ipynb>`__


.. _examples_as_discrete:

``as_discrete()`` function
^^^^^^^^^^^^^^^^^^^^^^^^^^

- `geom_smooth.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geom_smooth.ipynb>`__


.. _examples_export:

Export to File
^^^^^^^^^^^^^^

The ``ggsave()`` function is an easy way to export plot to a file in SVG
or HTML formats.

- `export_SVG_HTML.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/export_SVG_HTML.ipynb>`__


.. _examples_formatting:

Formatting
^^^^^^^^^^

- `formatting_axes_etc.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/formatting_axes_etc.ipynb>`__
- `label_format.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/label_format.ipynb>`__


.. _examples_theme:

Theme
^^^^^

Legend layout and axis presentation options:

- `legend_and_axis.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/legend_and_axis.ipynb>`__


.. _examples_sampling:

Data Sampling
^^^^^^^^^^^^^

Sampling is a special technique of data transformation, which helps to deal with large datasets and overplotting.

See examples in :ref:`Sampling in Lets-Plot <sampling>`.


.. _examples_tooltips:

Tooltip Customization
^^^^^^^^^^^^^^^^^^^^^

- `tooltip_config.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/tooltip_config.ipynb>`__
- Visualization of Airport Data on Map: |airport_data_kaggle|

.. |airport_data_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/alshan/visualization-of-airport-data-on-map

See also :ref:`Tooltip Customization <tooltips>`.


.. _examples_bistro:

The 'bistro' Package
^^^^^^^^^^^^^^^^^^^^

``from lets_plot.bistro.corr``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``corr_plot()``:
`correlation_plot.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/correlation_plot.ipynb>`__

``from lets_plot.bistro.im``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``image_matrix()``:
`image_matrix.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_matrix.ipynb>`__


.. _examples_geopandas:

GeoPandas Support
^^^^^^^^^^^^^^^^^

See examples in :ref:`GeoPandas Support <geopandas>`.


.. _examples_interactive_maps:

Interactive Maps
^^^^^^^^^^^^^^^^

The interactive map allows zooming in and out and panning around geospatial data that can be added to the base-map layer using regular ggplot2 'geoms'.

See examples in :ref:`Interactive Maps <interactive_maps>`.


.. _examples_geocoding:

Geocoding
^^^^^^^^^

Geocoding is the process of converting names of places into geographic coordinates.

See the "Examples" section in :ref:`Geocoding <geocoding>`.


.. _examples_miscellaneous:

Miscellaneous
^^^^^^^^^^^^^

- Getting started with BigQuery GIS and Lets-Plot: |bigquery_gis_kaggle|

.. |bigquery_gis_kaggle| image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg
    :width: 20px
    :height: 20px
    :alt: View at Kaggle
    :target: https://www.kaggle.com/asmirnovhoris/bigquery-gis-and-lets-plot