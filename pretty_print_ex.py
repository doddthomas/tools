#-----------------------------------------------------------------------
#
#   pretty_print_ex.py - a python script showing examples of pretty print
#                        package
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
 
import pprint
 
starwars = 'In a galaxy far, far, away, there once was an angry little sith vader that tried to rule all worlds'
count = {}
 
for character in starwars:
   count.setdefault(character,0)
   count[character] = count[character] + 1
 
print(count)
 
pprint.pprint(count)
