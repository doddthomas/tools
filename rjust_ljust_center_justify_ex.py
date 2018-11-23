#-----------------------------------------------------------------------
#
#   rjust_ljust_center_justify_ex.py - a python script showing examples
#                                      right, left, center justifying
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
print('Hello'.rjust(10))       #yields      Hello
print('Hello'.rjust(20))       #yields                Hello
print('Hello'.ljust(10))       #yields Hello
print('Hello'.rjust(20,'*'))   #yields ***************Hello
print('Hello'.ljust(20,'-'))   #yields Hello---------------
print('Hello'.center(20))      #yields        Hello       
print('Hello'.center(20,'='))  #yields =======Hello========
 
 
