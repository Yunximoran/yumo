import jieba


# jieba.lcut 切分中文词语
def jieba_split_count():
    s = input("请输入一个字符串")
    n = len(s)
    m = len(jieba.lcut(s))
    print("中文字符数{}， 中文词语数{}".format(n, m))


if __name__ == '__main__':
    jieba_split_count()
