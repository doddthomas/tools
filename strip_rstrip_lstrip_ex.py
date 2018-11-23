#-----------------------------------------------------------------------
#
#   strip_rstrip_lstrip_ex.py - a python script showing examples of
#                               stripping off whitespace
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
spam = '     Hello World     '
print('|' + spam.strip() + '|')     #yields |Hello World| 
print('|' + spam.rstrip() + '|')    #yields |     Hello World|
print('|' + spam.lstrip() + '|')    #yields |Hello World     |
 
