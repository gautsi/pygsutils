"""tools for caching, particularly pandas dataframes
"""
from pygsutils import general as g
from typing import Callable
import pandas as pd
from functools import wraps
import os
import logging


class DFCache:
    def __init__(self, loc: str):
        self.loc = loc
        g.make_dir(self.loc)

    def store(self, name: str) -> Callable[..., pd.DataFrame]:

        fp = f"{self.loc}/{name}.csv"

        def inner(func: Callable[..., pd.DataFrame]) -> Callable[..., pd.DataFrame]:
            @wraps(func)
            def wrapper(*args, **kwargs) -> pd.DataFrame:
                if os.path.isfile(fp):
                    logging.info(f"reading from cache at {fp}")
                    df = pd.read_csv(fp, dtype=object)
                else:
                    df = func(*args, **kwargs)
                    logging.info(f"saving to cache at {fp}")
                    df.to_csv(fp, index=False)
                return df
            return wrapper
        return inner
