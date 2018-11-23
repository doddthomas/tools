#-----------------------------------------------------------------------
#
#   str_equality_ex.py - a python script showing testing for string
#                        equality and if else statement
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
print('enter name=>',end=' ')
name = input()
if name == 'dodd':
    print('sup dodd')
elif name == 'andrea':
    print('sup andy')
else:
    print('do not know you ' + name)
