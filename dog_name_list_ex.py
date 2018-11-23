#-----------------------------------------------------------------------
#
#   dog_name_list_ex.py - a python script showing examples of dynamically
#                         adding items to an array/list
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
dogNames = []
 
while True:
   print('Enter dog name #' + str(len(dogNames)+1) + ' or [ENTER/RETURN] to exit=>',end=' ')
   name = input()
   if name =='':
      break
   dogNames = dogNames + [name]
 
print('Dog names:')
 
for name in dogNames:
   print(name)
