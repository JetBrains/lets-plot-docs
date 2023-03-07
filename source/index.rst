.. lets-plot documentation master file, created by
   sphinx-quickstart on Fri May 15 17:50:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. title:: Lets-Plot: open-source plotting library for statistical data


.. toctree::
    :glob:
    :hidden:
    :maxdepth: 1

    pages/charts
    pages/maps
    Geocoding <pages/geocoding>
    'bistro' plots <pages/bistro>
    What is new <pages/whats_new>

An Open-source Plotting Library for Statistical Data
====================================================

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

**Python versions:** 3.7-3.11

**OS:** Linux, macOS, Windows


Installation
------------

.. code:: shell

    pip install lets-plot

:ref:`requirements <requirements>`


Quickstart
----------

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

.. panels::
    :container: + lets-plot-platforms
    :column: col-lg-12 col-md-4 col-sm-6 col-xs-12 p-2

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


.. _index_meet_gog:

Meet the Grammar of Graphics
----------------------------

.. panels::
    :container: + gog-book
    :column: col-lg-2 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: /_static/images/ggplot2-elegant-graphics-for-data-analysis.jpg
        :target: https://ggplot2-book.org/index.html

    ---
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2

    Lets-Plot API is largely based on the :ref:`API <api>` provided by `ggplot2 <https://ggplot2.tidyverse.org>`__ package well-known to data scientists who use R.

    To learn more about the grammar of graphics, we recommend an excellent book called "ggplot2: Elegant Graphics for Data Analysis". This will be a good prerequisite for further exploration of the Lets-Plot library.


Explore Your Data with Lets-Plot
--------------------------------

.. panels::
    :container: + explore-your-data-container
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2
    :header: text-center

    :ref:`Charts <charts>`
    ^^^^^^^^^^^^^^^^^^^^^^

    .. raw:: html

        <a class="reference internal image-reference" href="pages/charts.html">
          <img src="_static/images/previews/charts.png">
        </a>

    ---
    :ref:`Maps <maps>`
    ^^^^^^^^^^^^^^^^^^

    .. raw:: html

        <a class="reference internal image-reference" href="pages/maps.html">
          <img src="_static/images/previews/maps.png">
        </a>

    ---
    :ref:`Geocoding <geocoding>`
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. raw:: html

        <a class="reference internal image-reference" href="pages/geocoding.html">
          <img src="_static/images/previews/geocoding.png">
        </a>


.. include:: /shared/features.rst