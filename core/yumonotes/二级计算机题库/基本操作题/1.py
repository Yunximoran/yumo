# 键盘输入
# format格式化输出
"""

:
填充
对齐
宽度
精度
类型
"""


def format_num():
    n = eval(input("请输入一个数字"))
    print("{:+^11}".format(chr(n - 1) + chr(n) + chr(n + 1)))


if __name__ == '__main__':
    format_num()
