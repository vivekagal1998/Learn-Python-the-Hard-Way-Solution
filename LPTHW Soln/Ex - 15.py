#sys is a package get argv from
#sys

from sys import argv

script, filename = argv

#txt make file objects 
txt = open(filename)

print("Here's your file %r: "%filename)
print("\n",txt.read(),"\n")

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
