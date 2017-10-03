from sys import argv

script, un = argv
prompt = '>'

print("Hi %s, I'm the %s script."%(un,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s"%un)
like = input(prompt)
print("Where do u live %s?"%un)
live = input(prompt)
print("What kind of computer do u have")
com = input(prompt)
print("""
Alright so u said %r about liking me.
You live in %r
Not sure Where that is.
And you have a %r computer. Nice.
"""%(like, live, com))
