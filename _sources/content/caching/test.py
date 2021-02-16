# %% [markdown]
"""
# Testing diskcache
"""

# %% tags=['hide-cell']
from IPython import get_ipython
if get_ipython() is not None:
    get_ipython().run_line_magic('load_ext', 'autoreload')
    get_ipython().run_line_magic('autoreload', '2')


# %%
import diskcache as d
import pandas as pd

# %%
cache = d.Cache("tmp")

# %%
df = pd.DataFrame([{"a": 1}])

# %%
cache["test_df"] = df

# %%
"test_df" in cache

# %%
cache.get("test_df", read=True)