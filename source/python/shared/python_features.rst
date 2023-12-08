.. include:: /python/shared/features.rst

.. grid:: 2
    :class-container: features-list

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/tooltips.svg

        Customizable Tooltips

        You can customize the content, values formatting and appearance of tooltip for any geometry layer in your plot. :ref:`Learn more <tooltips>`.

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/formatting.svg

        Formatting

        Lets-Plot supports formatting of numeric and date-time values in tooltips, legends, on the axes and text geometry layer. :ref:`Learn more <formats>`.

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/logo/kotlin.svg

        Kotlin API

        R, Python, what’s next? Right. `Lets-Plot Kotlin API <https://github.com/JetBrains/lets-plot-kotlin>`__ enables data visualization in JVM and Kotlin/JS applications as well as in scientific notebooks like Jupyter and Datalore.

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/sampling.svg

        Sampling

        Sampling is a special technique of data transformation, which helps to deal with large datasets and overplotting. :ref:`Learn more <sampling>`.

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/geospatial-visualization.svg

        Geospatial Visualization

        Find spatial objects with the help of our powerful and easy to use :ref:`Geocoding <geocoding>` module. In case you already have ``GeoDataFrame`` on hand - :ref:`plot it <geopandas>` straight away.

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/export.svg

        Export to SVG, PDF, HTML and PNG

        The :py:mod:`ggsave() <lets_plot.ggsave>` function is an easy way to export plot to a file in SVG, PDF, HTML or PNG formats. |export|.

        .. |export| extref:: export
            :type: text
            :text: Learn more

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/interactive-maps.svg

        Interactive Maps

        Interactive maps allow zooming and panning around your geospatial data with customizable vector or raster basemaps as a backdrop. :ref:`Learn more <maps>`.

    .. grid-item-card::
        :shadow: none

        .. image:: /_static/images/icons/features/offline-mode.svg

        'No Javascript' and Offline Mode

        In the 'no javascript' mode Lets-Plot generates plots as bare-bones SVG images. Plots in the notebook with option ``offline=True`` will be working without an Internet connection. :ref:`Learn more <no_js_and_offline_mode>`.