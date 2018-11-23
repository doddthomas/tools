#-----------------------------------------------------------------------
#
#   while_loop_break_ex.py - a python script showing example of while
#                            loop with break statement
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
spam = 0
while spam < 5:
    print('inside loop with spam=>' + str(spam))
    if spam == 3:
       break
    spam = spam +1
print('after loop with spam=>' + str(spam))
