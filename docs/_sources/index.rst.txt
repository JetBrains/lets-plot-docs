.. _index

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
    pages/geocoding

An Open-source Plotting Library for Statistical Data
====================================================

|jb-official| |latest-release| |license|

.. |jb-official| image:: https://jb.gg/badges/official-flat-square.svg
    :target: https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub
    :alt: JB Official
.. |latest-release| image:: https://img.shields.io/pypi/v/lets-plot?color=green&style=flat-square
    :target: https://pypi.org/project/lets-plot
    :alt: Latest release
.. |license| image:: https://img.shields.io/pypi/l/lets-plot?color=yellow&style=flat-square
    :target: https://opensource.org/licenses/MIT
    :alt: MIT License

**Python versions:** 3.6-3.9

**OS:** Linux, macOS, Windows


Installation
------------

.. code:: shell

    pip install lets-plot

Prerequisites
~~~~~~~~~~~~~

- `IPython <https://ipython.org>`__
- Windows users only: `MinGW toolchain <https://anaconda.org/msys2/m2w64-toolchain>`__

Datalore
~~~~~~~~

You can try Lets-Plot in `Datalore <https://datalore.jetbrains.com/view/notebook/Vl3fAET56UBray6rPufmDA>`__ where it is available out-of-the-box.


Quickstart
----------

.. jupyter-execute::
    :linenos:

    import numpy as np
    from lets_plot import *
    LetsPlot.setup_html()        

    np.random.seed(12)
    data = dict(
        cond=np.repeat(['A','B'], 200),
        rating=np.concatenate((np.random.normal(0, 1, 200), np.random.normal(1, 1.5, 200)))
    )

    ggplot(data, aes(x='rating', fill='cond')) + ggsize(500, 250) + \
        geom_density(color='dark_green', alpha=.7) + scale_fill_brewer(type='seq') + \
        theme(axis_line_y='blank')

.. raw:: html

    <div class="lets-plot-platforms">
      <div>
        <a class="reference external" href="https://nbviewer.jupyter.org/github/JetBrains/lets-plot/blob/master/docs/examples/jupyter-notebooks/quickstart.ipynb">
          <img src="_static/images/logo/jupyter.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://datalore.jetbrains.com/view/notebook/Vl3fAET56UBray6rPufmDA">
          <img src="_static/images/logo/datalore.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://plugins.jetbrains.com/plugin/14379-lets-plot-in-sciview">
          <img src="_static/images/logo/pycharm.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://www.kaggle.com/alshan/lets-plot-quickstart">
          <img src="_static/images/logo/kaggle.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://colab.research.google.com/drive/1uYYZcG0g0kP4lJdPkpWB8aBS96ioDii2?usp=sharing">
          <img src="_static/images/logo/colab.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://deepnote.com/project/673ea421-638e-469d-8d04-5cc4c6e0258f#%2Fnotebook.ipynb">
          <img src="_static/images/logo/deepnote.svg" />
        </a>
      </div>
    </div>


.. _index_meet_gog:

Meet the Grammar of Graphics
----------------------------

.. panels::
    :container: + gog-book
    :column: col-lg-2 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: _static/images/ggplot2-elegant-graphics-for-data-analysis.jpg
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