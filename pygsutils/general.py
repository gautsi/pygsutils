# general utilities

import logging
import requests
import os
import zipfile


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
    with requests.get(url) as r:
        with open(fp, "wb") as f:
            f.write(r.content)    

def extract_zip(path_to_zip, dest_folder):
    filename = path_to_zip.split("/")[-1]
    foldername = filename.split(".")[0]
    folderpath = f"{dest_folder}/{foldername}"
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    with zipfile.ZipFile(path_to_zip, "r") as zip_ref:
        zip_ref.extractall(folderpath)