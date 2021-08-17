"""
Guide
=====

Set legend type for each aesthetic: colorbar, legend, or none (no
legend).

"""

# sphinx_gallery_thumbnail_path = "gallery_py\_legends\_guide.png"

import pandas as pd

from lets_plot import *
LetsPlot.setup_html()

# %%

df = pd.read_csv('https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/mpg.csv')

# %%

# %% [markdown]
#
# Legend Guide
# ~~~~~~~~~~~~

# %%

ggplot(df, aes(x='fl')) + \
    geom_bar(aes(fill='manufacturer'), tooltips=layer_tooltips().line('@manufacturer')\
                                                                .line('fuel type|@fl')\
                                                                .line('count|@..count..')) + \
    scale_fill_discrete(guide=guide_legend(nrow=3)) + \
    ggsize(700, 400) + \
    theme(legend_position='bottom')

# %%

# %% [markdown]
#
# Colorbar Guide
# ~~~~~~~~~~~~~~

# %%

guide = guide_colorbar(nbin=40, barwidth=10, barheight=200)
ggplot(df, aes('cty', 'hwy')) + \
    geom_point(aes(color='hwy')) + \
    scale_color_gradient(trans='reverse', guide=guide)