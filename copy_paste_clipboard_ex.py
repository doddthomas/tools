#----------------------------------------------------------------
-------
#
#   copy_paste_clipboard_ex.py - a python script showing examples of
#                                copy/paste to/from clipboard
#
#---------------------    module history   -----------------------------
#
#   12-OCT-18 : PTR XXXX, Created, Dodd M. Thomas
#
#-----------------------------------------------------------------------
 
# sudo pip3 install pyperclip
import pyperclip
pyperclip.copy('Hello world!')
print(pyperclip.paste())         #yields 
