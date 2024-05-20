import os
import sys
import re
from lxml import etree

ROOTDIR = "\\".join(__file__.split("\\")[:-3])
ARGUMENTS = sys.argv[1:]


# 系统处理工具
def LOADCONFIG(XPath):
    """
        导入xml文件
    :return:
    """
    pass


def INITCONFIG(*args, **kwargs):
    print(ROOTDIR)


if __name__ == '__main__':
    INITCONFIG()
