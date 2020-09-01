# variable = {key: value}
myCat = {'size': 'fat', 'colour': 'brown', 'character': 'fricky'}
print(myCat['size'])

#items in a dictonary are unordered
[1, 2, 3] == [3, 1, 2]
#false
{'size': 'fat', 'colour': 'brown', 'character': 'fricky'} == \
{'size': 'fat', 'character': 'fricky', 'colour': 'brown'}
#true

eggs = {'chicken': 'beige', 'duck': 'brown', 'goose': 'white'}
print('chicken' in eggs) #true

#dictionary methods .keys(), .values(), .items()
print(eggs.keys())
print(eggs.values())
print(eggs.items())

for k, v in eggs.items():
    print(k, v)

# .get(), .setdefault()
print('The colour of crow eggs is ' + eggs.get('crow', 'not mentioned in our dictionary'))
print('The colour of chicken eggs is ' + eggs.get('chicken', 'not mentioned in our dictionary'))

eggs.setdefault('pigeon', 'blue')
print(eggs)
eggs.setdefault('pigeon', 'pink') #doesnt change anything
print(eggs)

#number of letters
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
letterCount = 0
for q in message:
    if q  is not ' ' and ',' and '.':
        letterCount += 1

print(letterCount)

#number of particular characters
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

print(count)

import pprint
pprint.pprint(count)