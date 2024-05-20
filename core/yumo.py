import string
import random

y1 = 'a'
y2 = 'asdf'

print(y1 in string.printable, y2 in string.printable)

print('abc' * 2, end=',')

s = 2
for i in range(1, 10):
    s += i
print(s)

ls = [1, 2, 3, 4, 5, 6, 7]    # join必须是字符串列表
print(''.join(str(ls).strip('[]').split(', ')))

