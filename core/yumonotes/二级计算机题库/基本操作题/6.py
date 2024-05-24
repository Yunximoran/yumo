from math import sqrt


def str_split_computing():
    ntxt = input("4个数字， 空格分隔")
    nls = ntxt.split(' ')
    
    x0 = int(nls[0])
    y0 = int(nls[1])
    x1 = int(nls[2])
    y1 = int(nls[3])

    # (a**2 + b**2)**0.5
    # pow 幂运算
    # sqrt 开根号
    r = sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))

    print("{:.2f}".format(r))


if __name__ == '__main__':
    str_split_computing()
