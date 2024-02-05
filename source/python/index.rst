.. lets-plot documentation master file, created by
   sphinx-quickstart on Fri May 15 17:50:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:orphan:

.. title:: Grammar of Graphics for Python

.. meta::
   :description: Lets-Plot is a multiplatform plotting library based on the Grammar of Graphics. It provides a ggplot2-like plotting API for Python and Kotlin users.
   :keywords: data visualization, geospatial visualization, python, grammar of graphics, ggplot2


.. _python-index:

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


.. _python-index-installation:

Installation
------------

.. code:: shell

    pip install lets-plot


.. _python-index-quick-start:

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
        theme(panel_grid_major_x='blank') + flavor_darcula()

.. raw:: html

    <script>
        const jupyterElements = document.getElementById("quick-start").getElementsByClassName("jupyter_container");
        jupyterElements[0].classList.add("only-light");
        jupyterElements[1].classList.add("only-dark");
    </script>

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


.. _python-index-user-guide:

User Guide
----------

.. grid:: 2

    .. grid-item-card::
        :columns: 3

        .. image:: /_static/images/coding_for_economists.png
            :target: https://aeturrell.github.io/coding-for-economists

    .. grid-item-card::
        :columns: auto

        *Coding for Economists* by Arthur Turrell

        - `Easy Data Visualisation for Tidy Data with Lets-Plot <https://aeturrell.github.io/coding-for-economists/vis-letsplot.html>`__ - how to make plots quickly using the declarative plotting.

.. grid:: 2

    .. grid-item-card::
        :columns: 3

        .. image:: /_static/images/Python4DS.png
            :target: https://aeturrell.github.io/python4DS/

    .. grid-item-card::
        :columns: auto

        *Python4DS* by Arthur Turrell

        - `Data Visualisation <https://aeturrell.github.io/python4DS/data-visualise.html>`__ - will teach you how to visualise your data using using Lets-Plot.

        - `Layers <https://aeturrell.github.io/python4DS/vis-layers.html>`__ - a deeper dive into aesthetic mappings, geometric objects, and facets.

        - `Exploratory Data Analysis <https://aeturrell.github.io/python4DS/exploratory-data-analysis.html>`__ - search for answers by visualising, transforming, and modelling your data.


.. _python-index-pages:

Explore Your Data with Lets-Plot
--------------------------------

.. grid:: 1
    :class-container: explore-your-data-container wide-grid wide-grid-1

    .. grid-item-card::
        :shadow: none

        .. raw:: html

            <a class="reference internal image-reference" href="pages/charts.html">
              <div class="container">
                <img src="../_static/images/previews/charts.png" alt="Charts">
                <div class="page-title">CHARTS</div>
              </div>
            </a>

    .. grid-item-card::
        :shadow: none

        .. raw:: html

            <a class="reference internal image-reference" href="pages/maps.html">
              <div class="container">
                <img src="../_static/images/previews/maps.png" alt="Maps">
                <div class="page-title">MAPS</div>
              </div>
            </a>

    .. grid-item-card::
        :shadow: none

        .. raw:: html

            <a class="reference internal image-reference" href="pages/geocoding.html">
              <div class="container">
                <img src="../_static/images/previews/geocoding.png" alt="Geocoding">
                <div class="page-title">GEOCODING</div>
              </div>
            </a>


.. include:: /python/shared/features.rst