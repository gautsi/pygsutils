# %% [markdown]
"""
# Testing cache
"""

# %% tags=['hide-cell']
from IPython import get_ipython

if get_ipython() is not None:
    get_ipython().run_line_magic("load_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")


# %%
from pygsutils import cache as c
import pandas as pd

# %%
class TestProcess:
    cache = c.DFCache(loc="./tmp")

    def __init__(self):
        self.df = pd.DataFrame([{"a": 3}])

    @property
    @cache.store(name="df_first")
    def df_first(self) -> pd.DataFrame:
        print("in df_first")
        return self.df.assign(b=1)

    @property
    @cache.store(name="df_second")
    def df_second(self) -> pd.DataFrame:
        print("in df_second")
        return self.df_first.assign(c=5)


# %%
tf = TestProcess()

# %%
tf.df_second

# %%
tf.df_second