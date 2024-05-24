a = [3, 6, 9]
b = eval(input("输入一个列表："))

sums = 0
# for i, j in zip(a, b):
#     sums += i * j

for i in range(len(a)):
    sums += a[i] * b[i]

print(sums)
