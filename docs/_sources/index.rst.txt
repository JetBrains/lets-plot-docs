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
=======

.. jupyter-execute::
    :linenos:

    import pandas as pd
    from lets_plot import *
    LetsPlot.setup_html()

    df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot/'
                     'master/docs/examples/data/titanic.csv')
    df = df.sort_values(by='Pclass')

    ggplot(df) + \
        geom_histogram(aes(x='Age', group='Survived', fill='Survived'), \
                       binwidth=5, center=0) + \
        facet_grid(x='Pclass', y='Sex') + \
        scale_x_continuous(name='age', breaks=list(range(0, 90, 10))) + \
        scale_fill_discrete(name='survived') + \
        ggsize(700, 400) + \
        ggtitle('Survival Rate on the Titanic: '
                'Distribution by Age, Gender and Class of Ticket')

|

.. panels::
    :column: col-md-4
    
    Contents
    ^^^^^^^^

    .. toctree::
        :maxdepth: 1

        _pages/installation
        _pages/quickstart
        api
        _pages/features
        gallery/index

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