from sys import argv
from os.path import exists

script, from1, to = argv

print("Copying from %s to %s "%(from1, to))

in_ = open(from1)
indata = in_.read()

print("The I/P file is %d bytes long"% len(indata))

print("Does the file exists? %r"% exists(to))

print("Ready! HIT Return to continue else CTRL + C")

input()

out = open(to,'a')
#out.write(indata)
indata.replace('copying','copied')
out.write("\n" + indata)
print("All Set")

out.close()
in_.close()

