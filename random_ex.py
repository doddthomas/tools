#-----------------------------------------------------------------------
#
#   random_ex.py - a python script showing example of random number
#                  generator
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
 
import random
for i in range(5):
   print(random.randint(1,100))


import numnpy as np
np.random.randint(1,100,5)

[random.randint(1,100) for i in range(5)]
