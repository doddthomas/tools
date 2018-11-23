#-----------------------------------------------------------------------
#
#   exception_ex.py - a python script showing example of trapping and
#                     handling a divide by zero exception error
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
def spam(divide_by):
   try:
        return 42 / divide_by
   except ZeroDivisionError:
        print('ERROR: invalid argument')
 
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
