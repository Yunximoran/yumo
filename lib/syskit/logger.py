import logging
import os.path
import re

import colorlog


class Logger:
    logger = logging.getLogger()

    __LEVEL = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    __COLORS = {
        "DEBUG": "blue",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red"
    }

    def __init__(self, name, setLevel="DEBUG", save=False):
        if setLevel and setLevel not in self.__LEVEL:
            raise "#"

        if setLevel in self.__LEVEL:
            self.logger.setLevel(self.__LEVEL[setLevel])
        else:
            self.logger.setLevel(logging.DEBUG)

        self.logger.name = name
        self.__CONF__(save)

    def __CONF__(self, save):
        log_format = "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        formatter = colorlog.ColoredFormatter(log_format, log_colors=self.__COLORS)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        if save:
            if not os.path.exists("log_info"):
                os.mkdir('log_info')
            file_handler = logging.FileHandler(f'log_info/{os.path.basename(__file__)}.log', 'w', encoding='utf-8')
            self.logger.addHandler(file_handler)

    def debug(self, *msg):
        def decorator(func):
            def wrap(*args, **kwargs):
                self.logger.debug(msg)
                res = func(*args, **kwargs)
                return res

            return wrap

        return decorator

    def info(self, *msg):
        def decorator(func):
            def wrap(*args, **kwargs):
                self.logger.info(msg)
                res = func(*args, **kwargs)
                return res

            return wrap

        return decorator

    def warning(self, *msg):
        def decorator(func):
            def wrap(*args, **kwargs):
                self.logger.warning(msg)
                res = func(*args, **kwargs)
                return res

            return wrap

        return decorator

    def error(self, *msg):
        def decorator(func):
            def wrap(*args, **kwargs):
                self.logger.error(msg)
                res = func(*args, **kwargs)
                return res

            return wrap

        return decorator

    def critical(self, *msg):
        def decorator(func):
            def wrap(*args, **kwargs):
                self.logger.critical(msg)
                res = func(*args, **kwargs)
                return res

            return wrap

        return decorator

    def __message__(self, msg):
        """

        :param msg:
        :return:
        """
        pass


if __name__ == '__main__':
    logger = Logger('yumonotes', 'DEBUG', False)


    @logger.record('test zero')
    def zero():
        print(1 / 0)


    zero()
