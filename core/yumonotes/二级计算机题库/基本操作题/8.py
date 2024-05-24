# 160\a
import sys


def computing():
    n = eval(input("请输入数量："))
    if n == 0:
        sys.exit()
    value = n * 160
    discount = 1
    if n > 1:
        if n <= 4:
            discount = 0.9
        elif n <= 9:
            discount = 0.8
        else:
            discount = 0.7
    print(discount)
    cost = discount * value
    print(cost)


if __name__ == '__main__':
    while True:
        computing()
