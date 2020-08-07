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
    for row in range(0, dim[0]):
        emptymatrix.append([])
        datainrow = input()

        for char in datainrow:
            if char != " ":
                emptymatrix[row].append(int(char))

                
getDimensions(dimA)   
createMatrix(dimA, matrixA)
print(matrixA)
