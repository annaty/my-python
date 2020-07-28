## .index() .append() .insert() .remove() .sort()

colours = ['pink', 'blue', 'yellow', 'green']
print(colours.index('yellow'))

colours.append('brown')
print(colours)

colours.insert(1, 'orange')
print(colours)

colours.remove('pink') #allows for picking a value
print(colours)
del colours[0] #allows for picking an index
print(colours)

numbers = [20, 43, 1, 12, 73, 49]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)

#we can't sort lists with both strings and numbers

stuff = ['Anna', 'Abby', 'align', 'acres']
#to sort strings that don't all start with a majuscule, use key = str.lower
stuff.sort(key = str.lower) 
print(stuff)