import numpy as np
import os

word = os.path.dirname(__file__)
os.chdir(word)
a = [1, 2, 3, 4, 5]
print(np.array(a))
print(a)


