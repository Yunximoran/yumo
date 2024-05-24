import random

random.seed(100)

s = 0
for i in range(3):
    n = random.randint(1, 9)
    s += pow(n, 3)
   
print(s)
