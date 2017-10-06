#let's work on dictionaries
'''stuff = {'name':'Vivek', 'age':18, 'height':6*2}

print(stuff['name'])
print(stuff['age'])

print(stuff)
'''
'''
state = {
    'Oregon'    : 'OR',
    'Florida'   : 'FL',
    'California': 'CA',
    'New York'  : 'NY',
    'Michigan'  : 'MI'
}

cities = {
    'CA': 'California',
    'NY'  : 'New York',
    'MI'  : 'Michigan'
}

cities['OR'] = 'Oregon'

cities['FL'] = 'Florida'

print('-'*10)
print("NY state has : ",cities['NY'])

print('-'*10)'''

a = {
    'a' : 'Monday',
    'b' : 'Tuesday',
    'c' : 'Wednesday',
    'd' : 'Thursday',
    'e' : 'Friday',
    'f' : 'Saturday',
    'g' : 'Sunday'
}

print(a)

for key,k in a.items():
    print(key, k)

print("-"*10)

print(a.get('a',"Hi there"))

print(a.get('h', "Hello World"))
