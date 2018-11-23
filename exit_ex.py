#-----------------------------------------------------------------------
#
#   exit_ex.py - a python script showing example of exiting to system
#                command line
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
 
import sys
 
while True:
    print('Type exit to exit=>', end=' ')
    response = input()
    if response == 'exit':
       sys.exit()
    print('you typed ' + response)
