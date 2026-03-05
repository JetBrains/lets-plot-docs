.. _annotations:

:og:description: You can customize the content and the view of annotations for pie and bar charts.

:orphan:

.. title:: Annotations in Lets-Plot

.. meta::
   :description: You can customize the content and the view of annotations for pie and bar charts.
   :keywords: annotation customization


Annotating Charts
=================

Lets-Plot provides several ways to annotate charts:

- **Label annotations for geometry layers.**
  Some geoms (such as pie, bar, and crossbar) support built-in text labels via the
  ``labels`` parameter. Pass the result of the :py:meth:`layer_labels() <lets_plot.layer_labels>`
  call to configure the label content and layout.

  |learn_more-annotations|.

.. |learn_more-annotations| extref:: annotations_page
    :type: text
    :text: Learn more (reference notebook)

- **Annotations for** :py:mod:`geom_smooth() <lets_plot.geom_smooth>`.
  Use the ``labels`` parameter together with :py:meth:`smooth_labels() <lets_plot.smooth_labels>`
  to display statistics computed by the ``smooth`` stat (for example, :math:`R^2`, adjusted :math:`R^2`,
  and a fitted model equation). ``smooth_labels`` extends ``layer_labels``, so formatting and text
  template helpers work the same way.

  |learn_more-smooth_annotations|.

.. |learn_more-smooth_annotations| extref:: smooth_summary
    :type: text
    :text: Learn more (reference notebook)

- **Bracket annotations.**
  Use :py:mod:`geom_bracket() <lets_plot.geom_bracket>` to add labeled brackets highlighting
  relationships between categories or marking an interval.
  Use :py:mod:`geom_bracket_dodge() <lets_plot.geom_bracket_dodge>` to draw brackets that connect
  *dodged* groups within each category (e.g., comparisons inside grouped boxplots/bars).

  |learn_more-brackets|.

.. |learn_more-brackets| extref:: geom_bracket
    :type: text
    :text: Learn more (reference notebook)

See also the :doc:`formatting reference </python/pages/formats>` to learn how to format numeric and date-time values in annotations.


Examples
--------

- .. extref:: geom_pie
      :type: text
- .. extref:: factor_levels
      :type: text
- .. extref:: named_system_colors
      :type: text
- .. extref:: titanic
      :type: text