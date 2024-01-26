.. _bistro:

.. title:: 'bistro' Plots

.. meta::
   :description: The 'bistro' package of Lets-Plot exists to help you with your EDA investigations by providing some useful charts right out of the box.
   :keywords: exploratory data analysis, EDA, correlation matrix, Q-Q plot, joint plot, residual plot


'bistro' Plots
==============

Exploratory Data Analysis (EDA) is an art of looking at one or more datasets in an effort to understand the underlying structure of the data contained there.

Below are a few instruments from the 'bistro' package that could help you with your EDA investigations.


.. _bistro_corr_plot:

Correlation Plot
----------------

:py:mod:`corr_plot() <lets_plot.bistro.corr.corr_plot>`

.. grid:: 4
    :class-container: preview-gallery wide-grid wide-grid-4

    .. grid-item-card::

        .. extref:: correlation_plot

    .. grid-item-card::

        .. extref:: correlation_plot
            :image: bistro-1

    .. grid-item-card::

        .. extref:: correlation_plot
            :image: bistro-2

    .. grid-item-card::

        .. extref:: correlation_plot
            :image: bistro-3


Examples:

- .. extref:: correlation_plot
      :type: text
- .. extref:: themes
      :type: text
- .. extref:: malnutrition
      :type: text


.. _bistro_qq_plot:

Q-Q Plot
--------

:py:mod:`geom_qq() <lets_plot.geom_qq>`,
:py:mod:`geom_qq_line() <lets_plot.geom_qq_line>`,
:py:mod:`geom_qq2() <lets_plot.geom_qq2>`,
:py:mod:`geom_qq2_line() <lets_plot.geom_qq2_line>`,
:py:mod:`qq_plot() <lets_plot.bistro.qq.qq_plot>`

.. grid:: 4
    :class-container: preview-gallery wide-grid wide-grid-4

    .. grid-item-card::

        .. extref:: qq_plots
            :image: bistro-1

    .. grid-item-card::

        .. extref:: qq_plots
            :image: bistro-2

    .. grid-item-card::

        .. extref:: qq_plots
            :image: bistro-3

    .. grid-item-card::

        .. extref:: qq_plots
            :image: bistro-4


Examples:

- .. extref:: qq_plots
      :type: text


.. _bistro_joint_plot:

Joint Plot
----------

:py:mod:`joint_plot() <lets_plot.bistro.joint.joint_plot>`

.. grid:: 4
    :class-container: preview-gallery wide-grid wide-grid-4

    .. grid-item-card::

        .. extref:: joint_plot
            :image: bistro-3

    .. grid-item-card::

        .. extref:: joint_plot
            :image: bistro-0

    .. grid-item-card::

        .. extref:: joint_plot
            :image: bistro-1

    .. grid-item-card::

        .. extref:: joint_plot
            :image: bistro-2


Examples:

- .. extref:: joint_plot
      :type: text


.. _bistro_residual_plot:

Residual Plot
-------------

:py:mod:`residual_plot() <lets_plot.bistro.residual.residual_plot>`

.. grid:: 4
    :class-container: preview-gallery wide-grid wide-grid-4

    .. grid-item-card::

        .. extref:: residual_plot

    .. grid-item-card::

        .. extref:: residual_plot
            :image: bistro-1

    .. grid-item-card::

        .. extref:: residual_plot
            :image: bistro-2

    .. grid-item-card::

        .. extref:: residual_plot
            :image: bistro-3


Examples:

- .. extref:: residual_plot
      :type: text