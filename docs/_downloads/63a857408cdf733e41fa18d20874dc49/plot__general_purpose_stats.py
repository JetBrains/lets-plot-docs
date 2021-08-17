"""
General Purpose Stats
=====================

Some plots visualize a transformation of the original data set. Use a
stat parameter to choose a common transformation to visualize.

Each stat creates additional variables to map aesthetics to. These
variables use a common ..name.. syntax.

Look at the examples of the most general stats below.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_stats\_general_purpose_stats.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')
df.head()

# %%

# %% [markdown]
#
# Identity Stat
# ~~~~~~~~~~~~~

# %%

w, h = 400, 300
p = ggplot() + ggsize(w, h)

p1 = p + geom_bar(aes(x='fl'), data=df) + \
         ggtitle('Default geom_bar() Stat - Count')

df2 = df.groupby('fl').median().iloc[:, 0].sort_values().to_frame('median').reset_index()
p2 = p + geom_bar(aes(x='fl', y='median'), data=df2, stat='identity') + \
         ggtitle('Identity Stat for Calculated Median')

p3 = p + geom_bin2d(aes('cty', 'hwy'), data=df) + \
         ggtitle('Default geom_bin2d() Stat - Count')

df4 = df.groupby(['cty', 'hwy']).median().iloc[:, 0].to_frame('median').reset_index()
p4 = p + geom_raster(aes(x='cty', y='hwy', fill='median'), data=df4, stat='identity') + \
         ggtitle('Identity Stat for Calculated Median')

bunch = GGBunch()
bunch.add_plot(p1, 0, 0)
bunch.add_plot(p2, w, 0)
bunch.add_plot(p3, 0, h)
bunch.add_plot(p4, w, h)
bunch