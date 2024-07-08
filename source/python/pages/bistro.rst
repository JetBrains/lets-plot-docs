.. _bistro:

:og:description: The 'bistro' package of Lets-Plot exists to help you with your EDA investigations by providing some useful charts right out of the box.

.. title:: Lets-Plot 'bistro': Streamline Your Eda With Ready-To-Use Charts

.. meta::
   :description: The 'bistro' package of Lets-Plot exists to help you with your EDA investigations by providing some useful charts right out of the box.
   :keywords: exploratory data analysis, EDA, correlation matrix, Q-Q plot, joint plot, residual plot


'bistro' Plots
==============

"Bistro" plots is a collection of "compound plots" allowing users to generate intricate charts without the need for extensive coding.

These plots build upon lets-plot's core functionality, combining multiple geoms, scales, and settings into ready-to-use functions.


.. _bistro_corr_plot:

Correlation Plot
----------------

:py:mod:`corr_plot() <lets_plot.bistro.corr.corr_plot>`

.. grid:: 4
    :class-container: preview-gallery wide-grid

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
    :class-container: preview-gallery wide-grid

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
    :class-container: preview-gallery wide-grid

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
    :class-container: preview-gallery wide-grid

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