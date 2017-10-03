from sys import argv

script, file = argv

print("And here's your file %r"%file)

text = open(file)

print("Let's try it once more time")
c = 1

while c <=2:
	file1 = input(">:Enter a file ")
 	text = open(file1)
	print(text.read())
	c+=1

print('''And here goes my code
	enjoy
	lfv
	)