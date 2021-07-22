.. _bistro:

.. include:: /shared/previews.rst

Bistro
======

The 'bistro' package is a collection of higher level API functions, each allows to create a certain kind of plot with a single function call instead of combining a plethora of plot features manually.

Correlation Plot
----------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |correlation-nbviewer|

    ---
    |corr_plot-nbviewer|

    ---
    |correlation_plot-nbviewer|

    ---
    |2020-nbviewer|

The ``corr_plot()`` function creates a fluent builder object offering a set of methods for configuring of beautiful correlation plots. A call to the terminal ``build()`` method in the end will create a resulting plot object.

Image Matrix
------------

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |basic_image_matrix-nbviewer|

    ---
    |image_matrix-nbviewer|

The ``image_matrix()`` function arranges a set of images in a grid.

The ``image_matrix()`` function uses geom_image under the hood, so you might want to check out these demos as well:

.. panels::
    :column: col-lg-3 col-md-4 col-sm-6 col-xs-12 p-2

    |image_101-nbviewer|

    ---
    |image_fisher_boat-nbviewer|

.. include:: /shared/features.rst