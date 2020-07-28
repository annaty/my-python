# list comprehension = shortening operations done on lists
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for number in a:
    if number % 2 == 0:
        b.append(number)
print(b)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
c = [number for number in a if number % 2 == 0]
print(c)


# print out the elements that are less than 5
d = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def lessThanFive(list):
    for element in list:
        if element < 5:
            print(element)
lessThanFive(d)

e = [number for number in d if number < 5]
print(e)

#program
print('Please specify a number between 2 and 100.')
userNumber = input()
def lessThanUserNumber(list):
    for element in list:
        if element < int(userNumber):
            print(element)

print('Here are the elements from list a that are smaller than your number: ')
lessThanUserNumber(a)
