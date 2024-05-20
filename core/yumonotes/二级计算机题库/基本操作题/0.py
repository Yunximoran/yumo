# jieba库
# 吃葡萄不吐葡萄皮 result：1.6
import jieba


# jieba.lcut(s) 精确模式， 返回一个列表类型

def jieba_split():
    txt = input("请输入一段中文文本")
    ls = jieba.lcut(txt)
    print(ls)
    print("{:.1f}".format(len(txt) / len(ls)))


if __name__ == '__main__':
    jieba_split()
