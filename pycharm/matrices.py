def launchProgram():
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. Exit")
    answer = input("Your choice: ")
    if answer == "0":
        quit()
    elif answer == "1":
        print("Enter the size of first matrix: ")
        dimA = getDimensions()
        print("Enter first matrix: ")
        mxA = createMatrix(dimA)
        print("Enter the size of second matrix: ")
        dimB = getDimensions()
        print("Enter second matrix: ")
        mxB = createMatrix(dimB)
        print("The result is: ")
        print(addMatrices(dimA, dimB, mxA, mxB))
        launchProgram()
    elif answer == "2":
        print("Enter size of matrix: ")
        dimA = getDimensions()
        print("Enter matrix: ")
        mxA = createMatrix(dimA)
        constant = input("Enter constant: ")
        print("The result is: ")
        print(multiByConst(mxA, constant))
        launchProgram()
    elif answer == "3":
        print("Enter the size of first matrix: ")
        dimA = getDimensions()
        print("Enter first matrix: ")
        mxA = createMatrix(dimA)
        print("Enter the size of second matrix: ")
        dimB = getDimensions()
        print("Enter second matrix: ")
        mxB = createMatrix(dimB)
        print("The result is: ")
        print(multiMatrices(dimA, dimB, mxA, mxB))
        launchProgram()
    elif answer == "4":
        print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        answer = input("Your choice: ")
        if answer == "1":
            print("Enter matrix size: ")
            dimA = getDimensions()
            print("Enter matrix: ")
            mxA = createMatrix(dimA)
            print("The result is: ")
            print(tMainDiag(dimA, mxA))
            launchProgram()
        elif answer == "2":
            print("Enter matrix size: ")
            dimA = getDimensions()
            print("Enter matrix: ")
            mxA = createMatrix(dimA)
            print("The result is: ")
            print(tSideDiag(dimA, mxA))
            launchProgram()
        elif answer == "3":
            print("Enter matrix size: ")
            dimA = getDimensions()
            print("Enter matrix: ")
            mxA = createMatrix(dimA)
            print("The result is: ")
            print(tVertLine(dimA, mxA))
            launchProgram()
        elif answer == "4":
            print("Enter matrix size: ")
            dimA = getDimensions()
            print("Enter matrix: ")
            mxA = createMatrix(dimA)
            print("The result is: ")
            print(tHoriLine(dimA, mxA))
            launchProgram()

def getDimensions():
    try:
        dims = [int(_) for _ in input().split()]
        return dims
    except:
        dims = [float(_) for _ in input().split()]
        return dims
    
def createMatrix(dims):
    #creating the matrix from input 
    matrix = [input().split() for row in range(dims[0])]
    #transforming contents into integers
    try:
        matrix = [[int(element) for element in row]for row in matrix]
    except:
        matrix = [[float(element) for element in row]for row in matrix]
    return matrix

def addMatrices(dim1, dim2, mx1, mx2):
    if dim1 != dim2:
        print("ERROR")
    else:
        result = [[mx1[row][element] + mx2[row][element] for element in range(0, dim1[1])] for row in range(0, dim1[0])]
        return prettifyResult(result)

def multiByConst(matrix, const):
    try:
        result = [[element * int(const) for element in row] for row in matrix]
    except:
        result = [[element * float(const) for element in row] for row in matrix]
    return prettifyResult(result)

def multiMatrices(dim1, dim2, mx1, mx2):
    if dim1[1] != dim2[0]:
        return "The operation cannot be performed."
    else:
        #source 
        #https://www.geeksforgeeks.org/python-program-multiply-two-matrices/
        result = [[0 for b in range(dim2[1])]for a in range(dim1[0])]
        for i in range(dim1[0]):
            for j in range(dim2[1]):
                for k in range(dim2[0]):
                    result[i][j] += mx1[i][k] * mx2[k][j]
        return prettifyResult(result)

def tMainDiag(dims, matrix):
    result = [[0 for b in range(dims[1])]for a in range(dims[0])]
    for row in range(dims[0]):
        for element in range(dims[1]):
            result[element][row] = matrix[row][element]
    return prettifyResult(result)

def tSideDiag(dims, matrix):
    result = [[0 for b in range(dims[1])]for a in range(dims[0])]
    for row in range(dims[0]):
        for element in range(dims[1]):
            result[-(element + 1)][-(row + 1)] = matrix[row][element]
    return prettifyResult(result)

def tVertLine(dims, matrix):
    result = [[0 for b in range(dims[1])]for a in range(dims[0])]
    for row in range(dims[0]):
        for element in range(dims[1]):
            result[row][-(element + 1)] = matrix[row][element]
    return prettifyResult(result)

def tHoriLine(dims, matrix):
    result = [[0 for b in range(dims[1])]for a in range(dims[0])]
    for row in range(dims[0]):
        for element in range(dims[1]):
            result[-(row + 1)][element] = matrix[row][element]
    return prettifyResult(result)

def prettifyResult(matrix):
    matrix = [[str(element) for element in row] for row in matrix]
    #source
    # https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python
    return "\n".join([" ".join(["{:1}".format(element) for element in row]) for row in matrix])
        
launchProgram()