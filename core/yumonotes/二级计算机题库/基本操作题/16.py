

a = [3, 6, 9]
b = eval(input("list"))
j = 1
for i in range(len(a)):
    b.insert(j, a[i])
    j += 2

print(b)
