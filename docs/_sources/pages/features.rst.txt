.. _features:

.. include:: /shared/previews.rst

Hot Features
============

.. panels::
    :container: + page-demo
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2
    :body: text-center

    Try the demo notebook with key features of Lets-Plot right now:

    .. image:: https://mybinder.org/badge_logo.svg
        :target: #
        :width: 100%

    (it's free and no need to sign-up)

    ---
    :column: col-lg-8 col-md-4 col-sm-6 col-xs-12 p-2

    |scatter_matrix_4x3-nbviewer|


GGBunch
-------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |ggbunch-nbviewer|

    ---
    |geom_smooth-nbviewer|

    ---
    |scatter_matrix-nbviewer|

GGBunch allows to show a collection of plots on one figure. Each plot in the collection can have arbitrary location and size. There is no automatic layout inside the bunch.


Correlation Plot
----------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |correlation_plot-nbviewer|

The ``corr_plot()`` function creates a fluent builder object offering a set of methods for configuring of beautiful correlation plots. A call to the terminal ``build()`` method in the end will create a resulting plot object.


Image Matrix
------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |image_matrix-nbviewer|

The ``image_matrix()`` function arranges a set of images in a grid.

The ``image_matrix()`` function uses geom_image under the hood, so you might want to check out these demos as well:

- `image_101.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_101.ipynb>`__
- `image_fisher_boat.ipynb <https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/image_fisher_boat.ipynb>`__


Formatting
----------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |formatting_axes_etc-nbviewer|

    ---
    |label_format-nbviewer|

    ---
    |facets-nbviewer|

    ---
    |map_airports-kaggle|

Lets-Plot supports formatting of values of numeric and date-time types.

Complementary to the value formatting, a *string template* is also supported.

Learn more: :ref:`Formatting <formats>`.


Tooltip Customization
---------------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |tooltip_config-nbviewer|

    ---
    |map_airports-kaggle|

You can customize the content of tooltips for the layer by using the parameter ``tooltips`` of ``geom`` functions.

Learn more: :ref:`Tooltip Customization <tooltips>`.


Data Sampling
-------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |sampling_random-nbviewer|

    ---
    |sampling_pick-nbviewer|

    ---
    |sampling_systematic-nbviewer|

    ---
    |sampling_stratified-nbviewer|

    ---
    |sampling_groups-nbviewer|

    ---
    |sampling_vertex-nbviewer|

Sampling is a special technique of data transformation, which is built into Lets-Plot and is applied after ``stat`` transformation.

Sampling helps dealing with large datasets when unintentional attempt to plot an excessively large number of geometries can lead to UI freezes and even to out-of-memory crashes.

Sampling is also one of the ways of handling over-plotting.

Learn more: :ref:`Sampling in Lets-Plot <sampling>`.


Export to File
--------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |export_svg_html-nbviewer|

The ``ggsave()`` function is an easy way to export plot to a file in SVG or HTML formats.

.. note::

    The ``ggsave()`` function currently do not save images of interactive maps to SVG.


'No Javascript' Mode
--------------------

In the 'no javascript' mode Lets-Plot genetares plots as bare-bones SVG images.

This mode is helpful when there is a requirement to render notebooks in an 'ipnb' renderer which does not suppopt javascript (like GitHub's built-in renderer).

Activate 'no javascript' mode using the ``LetsPlot.setup_html()`` method call:

.. code:: python

    from lets_plot import *
    LetsPlot.setup_html(no_js=True)

Alternativaly, you can set up the environment variable:

.. code:: bash

    LETS_PLOT_NO_JS = true   (other accepted values are: 1, t, y, yes)

.. note::

    Interactive maps do not support the 'no javascript' mode.


Offline Mode
------------

In classic Jupyter notebook the ``LetsPlot.setup_html()`` statement by default pre-loads Lets-Plot JS library from CDN. Alternatively, option ``offline=True`` will force Lets-Plot adding the full JS bundle to the notebook. In this case, plots in the notebook will be working without an Internet connection.

.. code:: python

   from lets_plot import *
   LetsPlot.setup_html(offline=True)

.. note::

    Internet connection is still required for interactive maps and geocoding API.