#-----------------------------------------------------------------------
#
#   strings_ex.py - a python script showing examples of substrings,
#                   newlines, and apostrophe escaping
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
 
print("Hello there!\nHow are you?\nI\'m doing fine.")
#Hello there!
#How are you?
#I'm doing fine.
print('''To Whom It May Concern,
 
Punk's cat has been arrested for catnapping, cat burglary, and just for being a cat.
 
Respectfully Yours,
Timmy''')
 
spam = 'Hello world!'
print(spam[:5])  #yields Hello
print(spam[6:])  #yields world!
print(spam[0:5]) #yields Hello
 
print(spam.upper()) #yields HELLO WORLD!
print(spam.lower()) #yields hello world!
 
