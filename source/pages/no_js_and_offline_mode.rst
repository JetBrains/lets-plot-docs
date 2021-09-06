.. _no_js_and_offline_mode:

'No Javascript' Mode
====================

In the 'no javascript' mode Lets-Plot genetares plots as bare-bones SVG images.

This mode is halpfull when there is a requirement to render notebooks in an 'ipnb' renderer which does not suppopt javascript (like GitHub's built-in renderer).

Activate 'no javascript' mode using the ``LetsPlot.setup_html()`` method call:

.. code:: python

    from lets_plot import *

    LetsPlot.setup_html(no_js=True)

Alternativaly, you can set up the environment variable:

::

    LETS_PLOT_NO_JS = true   (other accepted values are: 1, t, y, yes)

Note: interactive maps do not support the 'no javascript' mode.

Offline Mode
============

In classic Jupyter notebook the ``LetsPlot.setup_html()`` statement by default pre-loads ``Lets-Plot`` JS library from CDN.
Alternatively, option ``offline=True`` will force ``Lets-Plot`` adding the full Lets-Plot JS bundle to the notebook.
In this case, plots in the notebook will be working without an Internet connection.

.. code:: python

    from lets_plot import *

    LetsPlot.setup_html(offline=True)

Note: internet connection is still required for interactive maps and geocoding API.