"""tools for caching, particularly pandas dataframes
"""
from pygsutils import general as g
from typing import Callable, Optional, Dict, Union, List
import pandas as pd
from functools import wraps, cached_property
import os
import logging
import json
from dataclasses import dataclass

@dataclass
class Spec:
    loc: Optional[str] = None

spec = Spec()

def set_loc(new_loc: str) -> None:
    spec.loc = new_loc


class Cache:
    def __init__(self, InputType: type, ext: str, name: str):
        assert spec.loc is not None, "loc not set"
        g.make_dir(spec.loc)
        self.InputType = InputType
        self.ext = ext
        self.name = name

    @property
    def fp(self) -> str:
        return f"{spec.loc}/{self.name}.{self.ext}"

    @cached_property
    def read(self):  # -> self.InputType
        pass

    def write(self, obj) -> None:  # obj has type self.InputType
        pass

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> self.InputType:
            if os.path.isfile(self.fp):
                logging.info(f"reading from cache at {self.fp}")
                result = self.read
            else:
                result = func(*args, **kwargs)
                logging.info(f"saving to cache at {self.fp}")
                self.write(result)
            return result

        return wrapper


class DFCache(Cache):
    def __init__(self, name: str):
        super().__init__(InputType=pd.DataFrame, ext="csv", name=name)

    @property
    def read(self) -> pd.DataFrame:
        return pd.read_csv(self.fp, dtype=object)

    def write(self, obj: pd.DataFrame) -> None:
        obj.to_csv(self.fp, index=False)


JSONType = Union[List, Dict]


class JSONCache(Cache):
    def __init__(self, name: str):
        super().__init__(InputType=JSONType, ext="json", name=name)

    @property
    def read(self) -> JSONType:
        return json.load(self.fp)

    def write(self, obj: JSONType) -> None:
        with open(self.fp, "w") as f:
            json.dump(obj, f)