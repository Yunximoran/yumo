# import xml.etree.ElementTree as et
# import logging
# import colorlog
# import os
#
#
# class LogsManager:
#     workPath = os.getcwd()
#     baseName = os.path.basename(workPath)
#
#     __colors = {
#         "DEBUG": "blue",
#         "INFO": "green",
#         "WARNING": "yellow",
#         "ERROR": "red",
#         "CRITICAL": "red"
#     }
#
#     def __init__(self, name, attr):
#         self.logger = logging.getLogger(name)
#         self.logger.setLevel(logging.DEBUG)
#
#         console_handler = logging.StreamHandler()
#         file_handler = logging.FileHandler(f'{name}.logs', 'w')
#
#         logs_format = f"%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#         # formatter = logging.Formatter(logs_format)
#         formatter = colorlog.ColoredFormatter(logs_format, log_colors=self.__colors)
#
#         console_handler.setFormatter(formatter)
#
#         self.logger.addHandler(console_handler)
#         self.logger.addHandler(file_handler)
#
#
# if __name__ == '__main__':
#     logger = LogsManager('yumo', 'YuMo\\lib\\LogsManager')
#     logger.logger.debug('Hello')
#     logger.logger.info('Hello')
#     logger.logger.warning('Hello')
#     logger.logger.error('Hello')
#     logger.logger.critical('Hello')
