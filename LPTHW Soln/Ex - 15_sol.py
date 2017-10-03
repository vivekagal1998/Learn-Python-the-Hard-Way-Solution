#sys is a package get argv from
#sys

from sys import argv

script, filename = argv

#txt make file objects 
txt = open(filename)

print("Here's your file %r: "%filename)
print("\n",txt.read(),"\n")

txt.close()

#print("Type the filename again: ")

text = open(script)

print(text.read())

text.close()