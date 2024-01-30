.. lets-plot documentation master file, created by
   sphinx-quickstart on Fri May 15 17:50:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:orphan:

.. title:: Grammar of Graphics for Python

.. meta::
   :description: Lets-Plot is a multiplatform plotting library based on the Grammar of Graphics. It provides a ggplot2-like plotting API for Python and Kotlin users.
   :keywords: data visualization, geospatial visualization, python, grammar of graphics, ggplot2


Get Started
===========

.. image:: https://jb.gg/badges/official-flat-square.svg
    :target: https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub
    :alt: JB Official
.. image:: https://img.shields.io/pypi/v/lets-plot?color=green&style=flat-square
    :target: https://pypi.org/project/lets-plot
    :alt: Latest release
.. raw:: html

    <a class="reference internal image-reference" href="pages/licenses.html">
      <img alt="MIT License" src="https://img.shields.io/pypi/l/lets-plot?color=yellow&amp;style=flat-square">
    </a>

**Python versions:** 3.7-3.12

**OS:** Linux, macOS, Windows


Installation
------------

.. code:: shell

    pip install lets-plot


Quick Start
-----------

.. jupyter-execute::
    :linenos:

    import numpy as np
    from lets_plot import *
    LetsPlot.setup_html()        

    np.random.seed(12)
    data = dict(
        cond=np.repeat(['A', 'B'], 200),
        rating=np.concatenate((np.random.normal(0, 1, 200), np.random.normal(1, 1.5, 200)))
    )

    ggplot(data, aes(x='rating', fill='cond')) + ggsize(700, 300) + \
        geom_density(color='dark_green', alpha=.7) + scale_fill_brewer(type='seq') + \
        theme(panel_grid_major_x='blank')

.. extref:: quickstart
    :type: logo
    :ref: nbviewer
    :title: NBViewer

.. extref:: quickstart
    :type: logo
    :ref: datalore
    :title: Datalore

.. extref:: quickstart
    :type: logo
    :ref: kaggle
    :title: Kaggle

.. extref:: quickstart
    :type: logo
    :ref: colab
    :title: Google Colab

.. extref:: quickstart
    :type: logo
    :ref: deepnote
    :title: Deepnote
    :height: 3.2rem

.. extref:: quickstart
    :type: logo
    :ref: nextjournal
    :title: Nextjournal

.. extref:: quickstart
    :type: logo
    :ref: pycharm
    :title: PyCharm


References
----------

.. include:: /python/shared/books.rst


Explore Your Data with Lets-Plot
--------------------------------

.. grid:: 3
    :class-container: explore-your-data-container wide-grid wide-grid-3

    .. grid-item-card:: :ref:`Charts <charts>`
        :shadow: none

        .. raw:: html

            <a class="reference internal image-reference" href="pages/charts.html">
              <img src="../_static/images/previews/charts.png">
            </a>

    .. grid-item-card:: :ref:`Maps <maps>`
        :shadow: none

        .. raw:: html

            <a class="reference internal image-reference" href="pages/maps.html">
              <img src="../_static/images/previews/maps.png">
            </a>

    .. grid-item-card:: :ref:`Geocoding <geocoding>`
        :shadow: none

        .. raw:: html

            <a class="reference internal image-reference" href="pages/geocoding.html">
              <img src="../_static/images/previews/geocoding.png">
            </a>


.. include:: /python/shared/features.rst