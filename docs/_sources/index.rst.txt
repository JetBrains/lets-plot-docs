.. _index

.. lets-plot documentation master file, created by
   sphinx-quickstart on Fri May 15 17:50:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: /shared/previews.rst


An Open-source Plotting Library for Statistical Data
====================================================

|jb-official| |latest-release| |license|

.. |jb-official| image:: http://jb.gg/badges/official-flat-square.svg
    :target: https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub
.. |latest-release| image:: https://badge.fury.io/py/lets-plot.svg
    :target: https://pypi.org/project/lets-plot
.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT

**Python versions:** 3.6-3.9

**OS:** Linux, macOS, Windows


Installation
------------

.. code:: shell

    pip install lets-plot

Prerequisites
~~~~~~~~~~~~~

- `IPython <http://ipython.org>`__
- `Requests <https://docs.python-requests.org>`__ (only required for :ref:`geocoding <geocoding>`)
- Windows users only: `MinGW toolchain <https://anaconda.org/msys2/m2w64-toolchain>`__

Datalore
~~~~~~~~

You can try the Lets-Plot library in `Datalore <https://view.datalore.io/notebook/Zzg9EVS6i16ELQo3arzWsP>`__ where it is available out-of-the-box.


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
          <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://view.datalore.io/notebook/Zzg9EVS6i16ELQo3arzWsP">
          <img src="https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_datalore.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://plugins.jetbrains.com/plugin/14379-lets-plot-in-sciview">
          <img src="_static/images/logo/icon-pycharm.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://www.kaggle.com/alshan/lets-plot-quickstart">
          <img src="https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_kaggle.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://colab.research.google.com/drive/1uYYZcG0g0kP4lJdPkpWB8aBS96ioDii2?usp=sharing">
          <img src="https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_colab.svg" />
        </a>
      </div>
      <div>
        <a class="reference external" href="https://deepnote.com/project/673ea421-638e-469d-8d04-5cc4c6e0258f#%2Fnotebook.ipynb">
          <img src="https://raw.githubusercontent.com/JetBrains/lets-plot/master/docs/examples/images/logo_deepnote.svg" />
        </a>
      </div>
    </div>


Meet the Grammar of Graphics
----------------------------

.. panels::
    :container: + gog-book
    :column: col-lg-2 col-md-4 col-sm-6 col-xs-12 p-2

    .. image:: _static/images/ggplot2-elegant-graphics-for-data-analysis.jpg
        :target: https://ggplot2-book.org/index.html

    ---
    :column: col-lg-6 col-md-4 col-sm-6 col-xs-12 p-2

    The Lets-Plot for Python library provides an :ref:`API <api>` which is mostly based on the `ggplot2 <https://ggplot2.tidyverse.org>`__ package well-known to data scientists who use R.

    To learn more about the grammar of graphics, we recommend an excellent book called "ggplot2: Elegant Graphics for Data Analysis". It will be a good prerequisite for further exploration of the Lets-Plot library.


Explore Your Data with Lets-Plot
--------------------------------

.. panels::
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2
    :header: text-center

    Charts
    ^^^^^^

    .. raw:: html

        <a class="reference internal image-reference" href="pages/charts.html">
          <img src="_images/graph_building_4x3.png">
        </a>

    ---
    Maps
    ^^^^

    .. raw:: html

        <a class="reference internal image-reference" href="pages/maps.html">
          <img src="_images/museums_4x3.png">
        </a>

    ---
    Geocoding
    ^^^^^^^^^

    .. raw:: html

        <a class="reference internal image-reference" href="pages/geocoding.html">
          <img src="_images/geocoding_reference_4x3.png">
        </a>