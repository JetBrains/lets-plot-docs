.. _as_discrete:

.. title:: Function as_discrete() for ordering numeric data — Lets-Plot


Function ``as_discrete()``
==========================

The function :py:mod:`as_discrete() <lets_plot.mapping.as_discrete>` is used to annotate a numeric data series as categorical data with the possibility of its ordering for the purposes of given visualization.

Plot Preliminaries
------------------

.. jupyter-execute::

    import pandas as pd

    from lets_plot import *
    from lets_plot.mapping import as_discrete
    LetsPlot.setup_html()

    mpg = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

Usage
-----

.. code-block:: python

    as_discrete(variable, label=None, order_by=None, order=None)

where

- ``variable`` (string) - the name of the data variable (which is mapped to the plot aesthetic);
- ``label`` (string) - the name of the scale - it will be used as the axis label or as the legend title;
- ``order_by`` (string) - the name of the variable by which the ordering will be performed;
- ``order`` (int) - the ordering direction - ``1`` for ascending direction and ``-1`` for descending (default value).

To enable ordering mode, at least one ordering parameter (``order_by`` or ``order``) should be specified.
By the default, it will use descending direction and ordering by eigenvalues.
You cannot specify different order settings for the same variable. But if these settings don't contradict each other, they will be combined.


Examples
========

.. jupyter-execute::

    p = ggplot(mpg)
    p + geom_point(aes('displ', 'hwy', color='cyl'))

Let's annotate the ``'cyl'`` variable as discrete using the ``as_discrete('cyl')`` function.
As a result, the data is divided into groups, a discrete color scale is assigned instead of a continuous one:

.. jupyter-execute::

    p + geom_point(aes('displ', 'hwy', color=as_discrete('cyl')))

Set the ``'cyl'`` variable in ascending order of its values:

.. jupyter-execute::

    p + geom_point(aes('displ', 'hwy', color=as_discrete('cyl', order=1)))

Boxplot example:

.. jupyter-execute::

    p + geom_boxplot(aes('class', 'hwy'))

Order ``x`` alphabetically

.. jupyter-execute::

    p + geom_boxplot(aes(as_discrete('class', order=1), 'hwy'))

Order ``x`` by another variable - in descending order of the median:

.. jupyter-execute::

    p + geom_boxplot(aes(as_discrete('class', order_by='..middle..'), 'hwy'))

Add ``color`` associated with the same variable.
The ordering is also applied to it, which will be visible in the legend:

.. jupyter-execute::

    p + geom_boxplot(aes(as_discrete('class', order=1), 'hwy', color='class'))

Two different ordering settings are specified for the ``class`` variable. 
But these settings don't contradict each other. This means that they will be combined, and the variable will be ordered in ascending order ``ymax``:

.. jupyter-execute::

    p + geom_boxplot(aes(as_discrete('class', order_by='..ymax..'), 'hwy', color=as_discrete('class', order=1)))

Example of ordering for two variables:

.. jupyter-execute::

    p + geom_bar(aes(x=as_discrete('manufacturer', order=1), fill=as_discrete('class', order=1)), color='black')


Example Notebooks
=================

- .. extref:: ordering_examples
    :type: text
- .. extref:: geom_smooth_matrix
    :type: text