.. _index

.. lets-plot documentation master file, created by
   sphinx-quickstart on Fri May 15 17:50:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Lets-Plot
#########

**Lets-Plot** is an open-source plotting library for statistical data.

It is implemented using the `Kotlin programming language <https://kotlinlang.org>`_.


Example
-------

.. jupyter-execute::
    :linenos:

    import pandas as pd
    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

    ggplot(df, aes(x='cty')) + \
        geom_histogram(aes(fill='drv'), binwidth=1, center=df.cty.min()) + \
        scale_x_continuous(breaks=list(range(df.cty.min(), df.cty.max(), 6))) + \
        scale_fill_discrete() + \
        facet_grid(x='cyl', y='year') + \
        ggtitle('City Mileage by Drive Type, Number of Cylinders and Year of Manufacturing')

|

.. panels::
    :column: col-md-4
    
    Contents
    ^^^^^^^^

    .. toctree::
        :maxdepth: 1

        pages/installation
        pages/quickstart
        pages/api
        gallery/index
        pages/features

    ---

    Grammar of Graphics
    ^^^^^^^^^^^^^^^^^^^

    * :ref:`Plotting <api_plotting>`
    * :ref:`Geometries <api_geometries>`
    * :ref:`Facets and Scales <api_fs>`
    * :ref:`Positions and Coordinates <api_pc>`
    * :ref:`Theme <api_theme>`

    ---

    Features
    ^^^^^^^^

    * :ref:`GGBunch <features_ggbunch>`
    * :ref:`Data Sampling <features_sampling>`
    * :ref:`Export to File <features_export>`
    * :ref:`The 'bistro' Package <features_bistro>`
    * :ref:`Geospatial <features_geospatial>`
    * :ref:`'No Javascript' Mode <features_no_js>`
    * :ref:`Offline Mode <features_offline>`