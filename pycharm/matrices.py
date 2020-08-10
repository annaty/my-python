dimA = []
dimB = []
def getDimensions(dim):
    lenhi = input()
    for char in lenhi:
        if char != " ":
            dim.append(int(char))
      
matrixA = []
matrixB = []
def createMatrix(dim, emptymatrix):
    #create the empty list skeleton
    for row in range(0, dim[0]):
        emptymatrix.append([])
        datainput = input()

        #transform the datainput into integers and append them to the matrix
        for char in datainput:
            if char != " ":
                emptymatrix[row].append(int(char))

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

getDimensions(dimA)   
createMatrix(dimA, matrixA)
getDimensions(dimB)   
createMatrix(dimB, matrixB)
print(addMatrices(matrixA, matrixB))
