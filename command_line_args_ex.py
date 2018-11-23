#-----------------------------------------------------------------------
#
#   command_line_args_ex.py - a python script showing examples of using
#                             command line arguments
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
import sys
print('number of command line args=> ' + str(len(sys.argv)-1))
print('no command line arg=> ' + sys.argv[0])
print('one command line arg=> ' + sys.argv[1])
print('second command line arg=> ' + sys.argv[2])
