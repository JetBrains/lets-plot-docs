"""
1D Distributions
================

Some plots visualize a transformation of the original data set. Use a
``stat`` parameter to choose a common transformation to visualize.

Each stat creates additional variables to map aesthetics to. These
variables use a common ``..name..`` syntax.

Look at the examples of 1D distributions below.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_stats\_1d_distributions.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

p = ggplot(df, aes(x='hwy'))
p11 = p + geom_histogram() + ggtitle('stat="bin" (default)')
p12 = p + geom_histogram(stat='density') + ggtitle('stat="density"')
p21 = p + geom_density(stat='bin') + ggtitle('stat="bin"')
p22 = p + geom_density() + ggtitle('stat="density" (default)')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p11, 0, 0, w, h)
bunch.add_plot(p12, w, 0, w, h)
bunch.add_plot(p21, 0, h, w, h)
bunch.add_plot(p22, w, h, w, h)
bunch

# %%

p = ggplot(df, aes(x='fl'))
p1 = p + geom_bar() + ggtitle('stat="count" (default)')
p2 = p + geom_density(stat='count') + ggtitle('stat="count"')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch