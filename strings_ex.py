# -----------------------------------------------------------------------
#
#   strings_ex.py - a python script showing examples of substrings,
#                   newlines, and apostrophe escaping
#
# ---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
# -----------------------------------------------------------------------


print("Hello there!\nHow are you?\nI\'m doing fine.")
# yields =>
# Hello there!
# How are you?
# I'm doing fine.
print('''To Whom It May Concern,

Punk's cat has been arrested for catnapping, cat burglary, and just for being a cat.

Respectfully Yours,
Timmy''')

spam = 'Hello world!'
print(spam[:5])   # yields Hello
print(spam[6:])   # yields world!
print(spam[0:5])  # yields Hello

print(spam.upper())  # yields HELLO WORLD!
print(spam.lower())  # yields hello world!

# ------------------- Logan Editions -----------------------------------

# Note that you don't need to escape the quotes if mixing
print("Hello there! How are you? I\'m doing fine.")
# yields => Hello there! How are you? I'm doing fine.

print("Hello there! How are you? I'm doing fine.")
# yields => Hello there! How are you? I'm doing fine.

# print('Hello there! How are you? I'm doing fine.')
# yields =>
#   File "<ipython-input-2-67f3e347a3b0>", line 1
#     print('Hello there! How are you? I'm doing fine.')
#                                       ^
# SyntaxError: invalid syntax

# There is also a .title() method for strings
print('mr. bean'.title())
# yields => 'Mr. Bean'


# There are "justification" methods
s = 'tragdor'

print(s.center(20))
# yields => '      tragdor       '

print(s.ljust(20))
# yields => 'tragdor             '

print(s.rjust(20))
# yields => '             tragdor'

print(s.center(20, '-'))
# yields => '------tragdor-------'


# Other useful string methods
s = 'Dodd is the winner!'
print(s.replace('Dodd', 'Logan'))
# yields => 'Logan is the winner!'

print(s.split())
# yields => ['Dodd', 'is', 'the', 'winner!']

print(s.split(maxsplit=1))
# yields => ['Dodd', 'is the winner!']

print(s.rsplit(maxsplit=1))  # starts at the end of the string
# yields => ['Dodd is the', 'winner!']
