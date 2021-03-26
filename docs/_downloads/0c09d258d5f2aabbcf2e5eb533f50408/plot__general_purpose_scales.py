"""
General Purpose Scales
======================

Use with any aesthetic: alpha, color, fill, linetype, shape, size.

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_scales\_general_purpose_scales.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

# %% [markdown]
#
# Continuous Scales
# -----------------
# 
# Map continuous values to visual values.

# %%

p = ggplot(df, aes(x='fl')) + geom_bar(aes(fill='fl'))
p1 = p + ggtitle('Default')
p2 = p + scale_fill_continuous() + ggtitle('With Scale')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch

# %%

# %% [markdown]
#
# Discrete Scales
# ---------------
# 
# Map discrete values to visual values.

# %%

p = ggplot(df, aes(x='cyl')) + geom_bar(aes(color='cyl'), size=3, fill='white')
p1 = p + ggtitle('Default')
p2 = p + scale_color_discrete() + ggtitle('With Scale')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch

# %%

# %% [markdown]
#
# Identity Scales
# ---------------
# 
# Use data values **as** visual values.

# %%

p = ggplot(df, aes(x='cyl')) + \
    geom_bar(aes(size='cyl'), color='#54278f', fill='#f2f0f7', show_legend=False)
p1 = p + ggtitle('Default')
p2 = p + scale_size_identity() + ggtitle('With Scale')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch

# %%

# %% [markdown]
#
# Manual Scales
# -------------
# 
# Map discrete values to manually chosen visual values.

# %%

alpha_values = [.4, .1, .8, .85, .9]
p = ggplot(df, aes(x='fl')) + \
    geom_bar(aes(alpha='fl'), color='#0c2c84', fill='#0c2c84')
p1 = p + ggtitle('Default')
p2 = p + scale_alpha_manual(values=alpha_values) + ggtitle('With Scale')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p1, 0, 0, w, h)
bunch.add_plot(p2, w, 0, w, h)
bunch