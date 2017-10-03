def just(c_count, b_count):
	print("You have %d cheeses!"%c_count)
	print("You have %d butter!"%b_count)
	print("Man that's enough for party!")
	print("Get a blanket!\n")

print("We can just give the functions numbers directly")

just(20, 30)

print("OR, we can use variables from our scripts")
amount_of_cheese = 10
amount_of_crackers = 10

just(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too: ",just(10+20, 5+6))

print("And we can combine")

just(amount_of_cheese+100,amount_of_crackers+1000)


