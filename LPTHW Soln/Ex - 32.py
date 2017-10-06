hairs = ['brown', 'blond', 'red']
eyes  = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

tc = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in tc:
	print("This is count %d"%number)

for fruit in fruits:
	print("A fruit of type: %s"%fruit)

for i in change:
	print("I got %r"%i)

elements = range(0,6) 

for i in elements:
	print("Adding %d to the list"% i)
	#elements.append(range(10,15))

for i in range(0,6):
	print("Element was: %d"%i)
