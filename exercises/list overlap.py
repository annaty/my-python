a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d = [element for element in a if element in b]
def commonElements(list1, list2):
    for element in list1:
        if element in list2 and element not in c:
            c.append(element)

#commonElements(a, b)
print(c)
print(d)

import random

e = random.sample(range(1, 50), 15)
f = random.sample(range(20, 90), 25)

commonElements(e, f)
print(c)