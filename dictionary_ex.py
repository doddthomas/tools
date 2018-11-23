#-----------------------------------------------------------------------
#
#   dictionary_ex.py - a python script showing examples of dictionary
#                      key-value pairs
#           
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
 
# dictionary denoted by braces and key-value pair
myDog = {'size':'fat', 'color':'orange', 'disposition':'no_bark'}
print(myDog)
print(myDog['color'])
 
for v in myDog.values():
    print(v)
 
for k in myDog.keys():
    print(k)
 
for i in myDog.items():
    print(i)
 
if myDog.get('color',0) != 0:
   print('color is a key value in the dictionary')
else:
   print('color is NOT a key value in the dictionary')
 
