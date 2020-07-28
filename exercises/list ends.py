a = [5, 10, 15, 20, 25]
b = []


#for i in range(0,2):
#    b.append(a[0])
#    a.sort(reverse = True)

#print(b)

def StartEndList(list1, emptyList):
    emptyList.append(list1[0])
    emptyList.append(list1[-1])
    print(emptyList)

StartEndList(a, b)