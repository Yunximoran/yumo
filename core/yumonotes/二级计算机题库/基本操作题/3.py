# 逆序词
import jieba


def jieba_split():
    txt = input("中文文本")
    ls = jieba.lcut(txt)
    for i in ls[::-1]:
        # ls 可切片 -> 列表
        print(i, end='')


if __name__ == '__main__':
    jieba_split()
