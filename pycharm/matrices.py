dimA = []
dimB = []
mxA = []
mxB = []

#def getDimensions(dimentionlist):
#    lenhi = input()
#    for char in lenhi:
#        if char != " ":
#            dimentionlist.append(int(char))
      
def createMatrix(emptydims, emptymatrix):
    emptydims = [int(_) for _ in input().split()]
    #creating the matrix from input, then transforming their content into integers
    emptymatrix = [input().split() for row in range(emptydims[0])]
    emptymatrix = [[int(element) for element in row]for row in emptymatrix]
    return emptydims


def addMatrices(mx1, mx2):
    result = []
    if dimA != dimB:
        print("ERROR")
    else:
        for row in range(0, dimA[0]):
            #on each iteration add a row
            result.append([])
            #adding the values from mx1 and mx2, and appending it to the list "result"
            for element in range(0, dimA[1]):
                addition = mx1[row][element] + mx2[row][element]
                result[row].append([addition])
    
    #making the result pretty
    counter = 0
    result_clean = []
    for row in result:
        if counter > 0:
            result_clean.append("\n")
        for element in row:
            result_clean.append(str(element).strip("[]"))
        counter += 1
    return " ".join(result_clean)

def multiByConst(matrix):
    const = int(input())
    result = []
    counter = 0
    for row in matrix:
        result.append([])
        for element in row:
            result[counter].append(element * const)
        counter += 1
    #making the result pretty
    counter1 = 0
    result_clean = []
    for row in result:
        if counter1 > 0:
            result_clean.append("\n")
        for element in row:
            result_clean.append(str(element).strip("[]") + " ")
        counter1 += 1
    return "".join(result_clean)


createMatrix(dimA, mxA)
print(dimA)
print(mxA)

