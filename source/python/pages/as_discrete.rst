.. _as_discrete:

:og:description: The as_discrete() function converts a column to a discrete scale and allows you to specify the order of its values.

:orphan:

.. title:: Ordering Categories, as_discrete()

.. meta::
   :description: The as_discrete() function converts a column to a discrete scale and allows you to specify the order of its values.
   :keywords: data visualization, categorical data, ordering, discrete scale, as_discrete


Working with Categorical Variables and the ``as_discrete()`` Function
=====================================================================

In data analysis and visualization, discrete data commonly appears as categorical variables. These can be classified as:

- Nominal: unordered categories (e.g., colors, names)
- Ordinal: categories with a meaningful order (e.g., education levels, rating scales)

When visualizing Pandas series in *Lets-Plot*, ordinal data can be represented using `Pandas Categorical <https://pandas.pydata.org/docs/user_guide/categorical.html>`__ type with the ordered parameter set to ``True`` and a specified category order. *Lets-Plot* will respect this ordering in the resulting visualizations.

Alternatively, *Lets-Plot* provides the :py:mod:`as_discrete() <lets_plot.mapping.as_discrete>` function, which offers similar capabilities for any data type, not limited to Pandas DataFrames. This function allows for flexible manipulation of discrete data, including:

1. Annotation of numeric data as discrete: This allows continuous variables to be treated as categorical for visualization purposes.
2. Specification of discrete variable ordering: The order can be based on the variable’s own values or the values of another variable.
3. Custom ordering through explicit "factor levels": This feature allows for manual specification of category order.

The :py:mod:`as_discrete() <lets_plot.mapping.as_discrete>` function thus allows for precise control over how categories are represented and ordered in plots, regardless of the original data format.

.. jupyter-execute::
    :hide-code:

    import pandas as pd

    from lets_plot import *
    LetsPlot.setup_html()

    mpg = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')


Usage
-----

.. code-block:: python

    as_discrete(variable, label=None, order_by=None, order=None, levels=None)

where

- ``variable : str`` - the name of the data variable (which is mapped to the plot aesthetic);
- ``label : str`` - the name of the scale - it will be used as the axis label or as the legend title;
- ``order_by : str`` - the name of the variable by which the ordering will be performed;
- ``order : int`` - the ordering direction - ``1`` for ascending direction and ``-1`` for descending (default value).
- ``levels : list`` - the list of values that defines a specific order of categories.

To enable ordering mode, at least one ordering parameter (``order_by`` or ``order``) should be specified. By the default, it will use descending direction and ordering by eigenvalues. You cannot specify different order settings for the same variable. However, if these settings don't contradict each other, they will be combined.

The ``order_by`` is a numeric variable, which values are used for reordering. It's also possible to use statistical variables. The reordering uses the average value. The exception is plots with the ``stack`` position adjustment, where multiple bars occupying the same ``x`` position are stacked atop one another: in this case, the sum is calculated to get the order of the stack sizes.


Examples
--------

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

Order ``x`` alphabetically:

.. jupyter-execute::

    p + geom_boxplot(aes(as_discrete('class', order=1), 'hwy'))

Order ``x`` by another variable - in descending order of the median:

.. jupyter-execute::

    p + geom_boxplot(aes(as_discrete('class', order_by='..middle..'), 'hwy'))

Add ``color`` associated with the same variable. The ordering is also applied to it, which will be visible in the legend:

.. jupyter-execute::

    p + geom_boxplot(aes(as_discrete('class', order=1), 'hwy', color='class'))

Two different ordering settings are specified for the ``class`` variable. These settings don't contradict each other.
This means that they will be combined, and the variable will be ordered in ascending order ``ymax``:

.. jupyter-execute::

    p + geom_boxplot(aes(as_discrete('class', order_by='..ymax..'), 'hwy', \
                         color=as_discrete('class', order=1)))

Use the ``levels`` parameter to specify the exact order for the variable:

.. jupyter-execute::

    custom_order = ['subcompact', 'compact', 'suv', 'minivan', 'midsize', 'pickup', '2seater']
    p + geom_boxplot(aes(as_discrete('class', levels=custom_order), 'hwy', color='class'))

The following example is similar to the previous one, but uses the categorical column:

.. jupyter-execute::

    mpg['cat_class'] = pd.Categorical(mpg['class'], categories=custom_order, ordered=True)
    ggplot(mpg) + geom_boxplot(aes('cat_class', 'hwy', color='cat_class'))

Example of ordering for two variables:

.. jupyter-execute::

    p + geom_bar(aes(x=as_discrete('manufacturer', order=1), \
                     fill=as_discrete('class', order=1)), \
                 color='black')

Reorder ``x`` by counts to get from highest on the left to lowest on the right:

.. jupyter-execute::

    p + geom_bar(aes(x=as_discrete('manufacturer', order_by='..count..'), \
                     fill=as_discrete('class', order=1)), \
                 color='black')

Apply sampling to the plot after reordering:

.. jupyter-execute::

    p + geom_bar(aes(x=as_discrete('manufacturer', order_by='..count..'), \
                     fill=as_discrete('class', order=1)), \
                 color='black', sampling=sampling_pick(4))


Example Notebooks
-----------------

- .. extref:: geom_smooth_matrix
    :type: text
- .. extref:: ordering_examples
    :type: text
- .. extref:: factor_levels
    :type: text
