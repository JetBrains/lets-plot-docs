"""
Size Scales
===========

Scales control how a plot maps data values to the visual values of an
aesthetic.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_scales\_size_scales.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p = ggplot(df, aes('cty', 'hwy')) + geom_point(aes(size='cyl'), shape=21, alpha=.2)

# %%

p1 = p + ggtitle('Default')
p2 = p + scale_size(range=[3, 6]) + ggtitle('With Scale')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch

# %%

p1 = p + ggtitle('Default')
p2 = p + scale_size_area() + ggtitle('With Scale')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch