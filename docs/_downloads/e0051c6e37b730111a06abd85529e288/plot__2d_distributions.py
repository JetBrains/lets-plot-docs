"""
2D Distributions
================

Some plots visualize a transformation of the original data set. Use a
stat parameter to choose a common transformation to visualize.

Each stat creates additional variables to map aesthetics to. These
variables use a common ..name.. syntax.

Look at the examples of 2D distributions below.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_stats\_2d_distributions.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

w, h = 400, 300
p = ggplot(df, aes('cty', 'hwy')) + ggsize(w, h)
p11 = p + geom_bin2d() + ggtitle('geom="bin2d" + default stat')
p12 = p + geom_point(aes(color='..count..'), stat='bin2d', size=3, shape=15) + \
          ggtitle('geom="point" + stat="bin2d"')
p21 = p + geom_density2d() + ggtitle('geom="density2d" + default stat')
p22 = p + geom_point(stat='density2d', size=.5) + ggtitle('geom="point" + stat="density2d"')

bunch = GGBunch()
bunch.add_plot(p11, 0, 0)
bunch.add_plot(p12, w, 0)
bunch.add_plot(p21, 0, h)
bunch.add_plot(p22, w, h)
bunch