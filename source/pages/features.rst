.. _features:

Features
########


.. _features_ggbunch:

GGBunch
=======

GGBunch allows to show a collection of plots on one figure. Each plot in the collection can have arbitrary location and size. There is no automatic layout inside the bunch.

- `ggbunch.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/ggbunch.ipynb>`_
- `geom_smooth.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/geom_smooth.ipynb>`_
- `scatter_matrix.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/scatter_matrix.ipynb>`_


.. _features_sampling:

Data Sampling
=============

Sampling is a special technique of data transformation, which helps dealing with large datasets and overplotting.

Learn more: :ref:`Data Sampling <features_sampling>`.


.. _features_export:

Export to File
==============

The ``ggsave()`` function is an easy way to export plot to a file in SVG or HTML formats.

Note: The ``ggsave()`` function currently do not save images of interactive maps to SVG.

Example notebook: `export_SVG_HTML <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/export_SVG_HTML.ipynb>`_


.. _features_bistro:

The 'bistro' Package
====================

The 'bistro' package is a collection of higher level API functions, each allows to create a certain kind of plot with a single function call instead of combining a plethora of plot features manually.

Correlation Plot
----------------

``from lets_plot.bistro.corr``

The ``corr_plot()`` function creates a fluent builder object offering a set of methods for configuring of beautiful correlation plots. A call to the terminal ``build()`` method in the end will create a resulting plot object.

Example: `correlation_plot.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/correlation_plot.ipynb>`_

Image Matrix
------------

``from lets_plot.bistro.im``

The ``image_matrix()`` function arranges a set of images in a grid.

Example: `image_matrix.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_matrix.ipynb>`_

The ``image_matrix()`` function uses ``geom_image`` under the hood, so you might want to check out these demos as well:

- `image_101.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_101.ipynb>`_
- `image_fisher_boat.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_fisher_boat.ipynb>`_


.. _features_geospatial:

Geospatial
==========

GeoPandas Support
-----------------

GeoPandas ``GeoDataFrame`` is supported by the following geometry layers: ``geom_polygon``, ``geom_map``, ``geom_point``, ``geom_text``, ``geom_rect``.

Learn more: :ref:`GeoPandas Support <features_geopandas_support>`.

.. image:: https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/kotlin_island.png
    :width: 480px
    :alt: Couldn't load kotlin_island.png

Interactive Maps
----------------

Interactive maps allow zooming and panning around geospatial data that can be added to the base-map layer using regular ggplot geoms.

Learn more: :ref:`Interactive Maps <features_interactive_maps>`.

Geocoding API
-------------

Geocoding is the process of converting names of places into geographic coordinates.

Learn more: :ref:`Geocoding API <features_geocoding_api>`.


.. _features_no_js:

'No Javascript' Mode
====================

In the 'no javascript' mode Lets-Plot genetares plots as bare-bones SVG images.

This mode is halpfull when there is a requirement to render notebooks in an 'ipnb' renderer which does not suppopt javascript (like GitHub's built-in renderer).

Activate 'no javascript' mode using the ``LetsPlot.setup_html()`` method call:

.. code-block:: python

    from lets_plot import *

    LetsPlot.setup_html(no_js=True)

Alternativaly, you can set up the environment variable::

    LETS_PLOT_NO_JS = true   (other accepted values are: 1, t, y, yes)

Note: interactive maps do not support the 'no javascript' mode.


.. _features_offline:

Offline Mode
============

In classic Jupyter notebook the ``LetsPlot.setup_html()`` statement by default pre-loads ``Lets-Plot`` JS library from CDN. Alternatively, option ``offline=True`` will force ``Lets-Plot`` adding the full Lets-Plot JS bundle to the notebook. In this case, plots in the notebook will be working without an Internet connection.

.. code-block:: python

    from lets_plot import *

    LetsPlot.setup_html(offline=True)

Note: internet connection is still required for interactive maps and geocoding API.