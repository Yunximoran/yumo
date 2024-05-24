data = ['综合', '理工', '综合', '综合', '文化', '文化', '综合']

d = {}

for da in data:
    if da not in d:
        d[da] = 1
    else:
        d[da] += 1



print(d)
