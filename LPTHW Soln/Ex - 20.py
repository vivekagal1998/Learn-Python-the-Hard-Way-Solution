from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def print_in_a_line(line_c, f):
	print(line_c, f.readline())

cur_file = open(input_file)

print("First let's print the whole file: \n")

print_all(cur_file)

print("Now let's rewind, kind of like a tape")

rewind(cur_file)

print("let's print three lines")

#print(range(5,10))

for cur_line in range(1,5):
	print_in_a_line(cur_line, cur_file)


