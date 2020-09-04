# -----------------------------------------------------------------------
#
#   random_ex.py - a python script showing example of random number
#                  generator
#
# ---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
# -----------------------------------------------------------------------


import random
print('from random for loop:')
for i in range(5):
    print(random.randint(1,100))


import numpy as np
print('from numpy array generation:')
print(np.random.randint(1,100,5))

print('from random list comprehension:')
rands = [random.randint(1,100) for i in range(5)]
print(rands)

# Can set seed with random or numpy to ensure state
random.seed(42)
print([random.random() for _ in range(5)])
# ALWAYS yields => [0.6394267984578837, 0.025010755222666936, 0.27502931836911926, 0.22321073814882275, 0.7364712141640124]

np.random.seed(5)
print(np.random.randint(1,100,5))
# ALWAYS yields => [79 62 17 74  9]
