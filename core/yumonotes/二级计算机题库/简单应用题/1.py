stop = False
d = {}

s = 0
i = 0
max_num = None
min_num = None
while True:
    data = input()
    if not data:
        break
    i += 1
    course, num = data.split(" ")[0], eval(data.split(" ")[1])
    if course not in d:
        d[course] = num

    s += num

X = s / i
s = list(d.items())
s.sort(key=lambda x: x[1], reverse=True)
print(s[0], s[-1], X)
