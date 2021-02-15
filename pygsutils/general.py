# general utilities

import logging
import requests
import os
import zipfile
from functools import wraps
from typing import Union, Callable


def setup_logging(fp: str) -> None:
    """Sets up logging to file at fp and to stdout

    Arguments:
        fp {str} -- path to log file
    """
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)-5.5s] %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    rootLogger = logging.getLogger()

    fileHandler = logging.FileHandler(fp)
    fileHandler.setFormatter(formatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    rootLogger.addHandler(consoleHandler)

    rootLogger.setLevel(logging.DEBUG)

def download(url:str, fp:str) -> None:
    logging.info(f"downloading {url} to {fp}")
    with requests.get(url) as r:
        with open(fp, "wb") as f:
            f.write(r.content)    

def extract_zip(path_to_zip:str, dest_folder:str) -> None:
    logging.info(f"extracting {path_to_zip} to {dest_folder}")
    with zipfile.ZipFile(path_to_zip, "r") as zip_ref:
        zip_ref.extractall(dest_folder)

def log_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            logging.exception(20*"-")
            raise
    return wrapper

def make_dir(dir_or_func:Union[str, Callable]) -> Union[None, Callable]:
    if type(dir_or_func) is str:
        if not os.path.exists(dir):
            os.makedirs(dir)
    elif callable(dir_or_func):
        @wraps(dir_or_func)
        def wrapper(*args, **kwargs):
            dir = dir_or_func(*args, **kwargs)
            if not os.path.exists(dir):
                os.makedirs(dir)
            return dir
        return wrapper
    else:
        raise(f"dir_or_func type not handled: {type(dir_or_func)}")