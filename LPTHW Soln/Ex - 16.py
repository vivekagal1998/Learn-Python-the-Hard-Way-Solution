from sys import argv

script, file_name = argv

tar1 = open(file_name)

print("We're going to erase %r."%file_name)

print("If you don't want that hit Ctrl + C")
print("If you do simply HIT return")

input("?")

print("Loading...\n")
print("Current contents of file are ",tar1.read())

tar = open(file_name,'w+')
print(tar.read())
'''var = input("Enter what you want to write... => ")

tar.write(var)
'''
print("Truncating Good Bye...")
tar.truncate()

l1 = input("Line 1 : ")
l2 = input("Line 2 : ")
l3 = input("Line 3 : ")

print("I will write on the file soon!")

tar.write(l1+"\n"+l2+"\n"+l3)

print("I am going to close this")
tar.close()