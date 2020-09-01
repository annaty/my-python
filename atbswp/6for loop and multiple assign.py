for i in range(4):
    print(i)
range(4) # = range(0, 4)
list(range(4)) # =[0, 1, 2, 3]
list(range(0, 100, 2))

colours = ['pink', 'blue', 'yellow', 'green']
for colour in range(len(colours)):
    print('The colour at index ' + str(colour) + ' in the list of coulours is ' + colours[colour])

### multiple assignment
cat = ['fat', 'orange', 'loud']
size = cat[0]
colour = cat[1]
disposition = cat[2]
##instead:
dog = ['small', 'brown', 'quiet']
size, colour, disposition = dog
print(colour)

##swapping variables
a = 'AAA'
b = 'BBB'

a, b = b, a
print(a, b)