# general utilities

import logging


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
