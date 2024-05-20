def format_num():
    n = eval(input('正整数'))
    print("{:->20,}".format(n))


if __name__ == '__main__':
    format_num()
