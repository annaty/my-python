def getDimensions():
    dims = [int(_) for _ in input().split()]
    return dims
    
def createMatrix(dims):
    #creating the matrix from input, then transforming their content into integers
    matrix = [input().split() for row in range(dims[0])]
    matrix = [[int(element) for element in row]for row in matrix]
    return matrix

def addMatrices(mx1, mx2):
    result = []
    if dimA != dimB:
        print("ERROR")
    else:
        result = [[mx1[row][element] + mx2[row][element] for element in range(0, dimA[1])] for row in range(0, dimA[0])]
        return result

def multiByConst(matrix):
    const = float(input())
    result = [[element * const for element in row] for row in matrix]
    return result

dimA = getDimensions()
mxA = createMatrix(dimA)
dimB = getDimensions()
mxB = createMatrix(dimB)


