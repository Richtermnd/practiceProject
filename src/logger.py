import logging
import json
import sys
from typing import Any


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


class Logger:
    def __init__(self, logger: logging.Logger):
        self.attrs = {}
        self.logger = logger

    def withAttrs(self, **kwargs):
        self.attrs |= kwargs

    def debug(self, msg: str, **kwargs):
        self.logger.debug(self._build_string(msg, **kwargs))

    def info(self, msg: str, **kwargs):
        self.logger.info(self._build_string(msg, **kwargs))
        self.logger.error
        
    def warning(self, msg: str, **kwargs):
        self.logger.warning(self._build_string(msg, **kwargs))

    def error(self, msg: str, **kwargs):
        self.logger.error(self._build_string(msg, **kwargs))

    def fatal(self, msg: str, **kwargs):
        self.logger.fatal(self._build_string(msg, **kwargs))
        exit(1)

    def _build_string(self, msg: str, **kwargs):
        return f"{msg}\n{json.dumps(kwargs | self.attrs, indent=2)}"


_logger_map = {}


def get_logger(name: str, level=logging.DEBUG):
    if name not in _logger_map:
        log = logging.getLogger(name)
        log.setLevel(level)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        log.addHandler(handler)
        logger = Logger(log)
    else:
        logger = _logger_map[name]
    return logger
