import os
import sys
import re
import logging
import colorlog

"""

"""

# 系统处理工具

def parseArgs():
    """
        解析传递参数
    """
    results = {}
    args = sys.argv

    index = 0
    for elem in args:
        match = re.search('=', elem)
        if match:  # 对于携带等号的参数 格式统一为：  key = [ value1, value2, ..., values ]
            s = match.start()  # 等号起始位置
            e = match.end()  # 等号结束位置

            key = elem[:s]  # key
            val = re.findall(r'[^\[\], ]+', elem[e:])  # '[val1, val2, ..., vals]'

            results[key] = val
        else:

            results[index] = elem
            index += 1

    return results


def logger(name):
    log_directory = os.path.dirname(__file__)

    logObj = logging.getLogger()
    logObj.setLevel(logging.DEBUG)
    logObj.name = name  # 名称可以后面定义

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f'{log_directory}/{name}.log', 'w', encoding='utf-8')

    log_format = f"%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_colors = {
        "DEBUG": "blue",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red"
    }
    formatter = colorlog.ColoredFormatter(log_format, log_colors=log_colors)

    console_handler.setFormatter(formatter)

    logObj.addHandler(console_handler)
    logObj.addHandler(file_handler)

    return logObj


if __name__ == '__main__':
    log = logger('sys')
    log.debug("test 这是一个 DEBUG")
    log.error("test 这是一个 ERROR")
    log.critical("test 这是一个 CRITICAL")
