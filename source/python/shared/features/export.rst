.. image:: /_static/images/icons/features/export-light.svg
    :class: only-light

.. image:: /_static/images/icons/features/export-dark.svg
    :class: only-dark

Export to SVG, HTML, PNG and PDF

Use the :py:func:`ggsave() <lets_plot.ggsave>` function to save your plot to a file. Alternatively, leverage the :py:meth:`to_svg() <lets_plot.plot.core.PlotSpec.to_svg>`, :py:meth:`to_html() <lets_plot.plot.core.PlotSpec.to_html>`, :py:meth:`to_png() <lets_plot.plot.core.PlotSpec.to_png>`, or :py:meth:`to_pdf() <lets_plot.plot.core.PlotSpec.to_pdf>` methods of the plot object to save it to a file or an in-memory file-like object. |export|.

.. |export| extref:: export
    :type: text
    :text: Learn more