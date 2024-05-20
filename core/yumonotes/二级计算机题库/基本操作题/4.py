# 随机选择一个手机品牌屏幕输出
import random

random.seed(0)

brandList = ['n1', 'n2', 'n3', 'n4', 'n5']
# index = random.randint(0, len(brandList))
# name = brandList[index]
name = random.sample(brandList, 1)  # 从序列中随机出去k个元素？
print(name)
