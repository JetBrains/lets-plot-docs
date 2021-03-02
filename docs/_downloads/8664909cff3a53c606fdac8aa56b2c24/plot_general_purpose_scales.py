"""
General Purpose Scales
======================

Use with any aesthetic: alpha, color, fill, linetype, shape, size.

"""

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

p = ggplot(df, aes(x='fl')) + \
    geom_bar(aes(fill='fl'))

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p + ggtitle('Default'), 0, 0, w, h)
bunch.add_plot(p + scale_fill_continuous() + \
               ggtitle('With Scale'), w, 0, w, h)
bunch.show()

# %%

# %% [markdown]
#
# Discrete Scales
# ---------------
# 
# Map discrete values to visual values.

# %%

p = ggplot(df, aes(x='cyl')) + \
    geom_bar(aes(color='cyl'), size=3, fill='white')

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p + ggtitle('Default'), 0, 0, w, h)
bunch.add_plot(p + scale_color_discrete() + \
               ggtitle('With Scale'), w, 0, w, h)
bunch.show()

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

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p + ggtitle('Default'), 0, 0, w, h)
bunch.add_plot(p + scale_size_identity() + \
               ggtitle('With Scale'), w, 0, w, h)
bunch.show()

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

w, h = 400, 300
bunch = GGBunch()
bunch.add_plot(p + ggtitle('Default'), 0, 0, w, h)
bunch.add_plot(p + scale_alpha_manual(values=alpha_values) + \
               ggtitle('With Scale'), w, 0, w, h)
bunch.show()