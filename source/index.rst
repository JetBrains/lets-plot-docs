.. _index

.. lets-plot documentation master file, created by
   sphinx-quickstart on Fri May 15 17:50:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: /shared/previews.rst


Explore Your Data with Lets-Plot
================================

|jb-official| |latest-release| |license|

.. |jb-official| image:: http://jb.gg/badges/official-flat-square.svg
    :target: https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub
.. |latest-release| image:: https://badge.fury.io/py/lets-plot.svg
    :target: https://pypi.org/project/lets-plot
.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT

The **Lets-Plot** for Python library includes a native backend and a :ref:`Python API <api>`, which was mostly based on the `ggplot2 <https://ggplot2.tidyverse.org>`__ package well-known to data scientists who use R.

To learn more about the grammar of graphics, we recommend an excellent book called "`ggplot2: Elegant Graphics for Data Analysis <https://ggplot2-book.org/index.html>`__". It will be a good prerequisite for further exploration of the **Lets-Plot** library.

.. panels::
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2

    Charts
    ^^^^^^

    .. raw:: html

        <a class="reference internal image-reference" href="pages/gog.html">
          <img src="_images/graph_building_4x3.png">
        </a>

    ---
    Maps
    ^^^^

    .. raw:: html

        <a class="reference internal image-reference" href="pages/interactive_maps.html">
          <img src="_images/museums_4x3.png">
        </a>

    ---
    Geocoding
    ^^^^^^^^^

    .. raw:: html

        <a class="reference internal image-reference" href="#">
          <img src="_images/geocoding_reference_4x3.png">
        </a>

Quickstart with Jupyter
-----------------------

You can use **Lets-Plot** in a Jupyter notebook or another notebook of your choice, like Datalore, Kaggle or Colab.

To evaluate the plotting capabilities of **Lets-Plot**, add the following code to a Jupyter notebook:

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

.. include:: /shared/features.rst