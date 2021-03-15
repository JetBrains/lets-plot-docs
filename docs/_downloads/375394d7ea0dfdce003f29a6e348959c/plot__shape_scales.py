"""
Shape Scales
============

Scales control how a plot maps data values to the visual values of an
aesthetic.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_scales\_shape_scales.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

fl_df = df.groupby(['cty', 'hwy']).fl.agg(pd.Series.mode).to_frame('fl').reset_index()
fl_df.head(2)

# %%

p = ggplot(fl_df, aes('cty', 'hwy')) + geom_point(aes(shape='fl'))
p

# %%

p + scale_shape(solid=False)

# %%

p + scale_shape_manual(values=[0, 12, 1, 10, 3, 13, 2, 4])