import numpy as np
def create():
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    rng = np.random.default_rng()
    mat = rng.integers(low=0,high=1,size=(row,column))
    for i in range(row):
        temp = [int(input(f"Enter element for row{i+1}: ")) for x in range(column)]
        for j in range(column):
            mat[i][j] = temp[j]
    print("\nMatrix :\n")
    print(mat)
    return mat
def add(a,b):
    try:
        print(a+b)
    except ValueError:
        print("unable to perform operation")
def sub(a,b):
    try:
        print(a-b)
    except ValueError:
        print("unable to perform operation")
def matmul(a,b):
    try:
        print(a@b)
    except ValueError:
        print("unable to perform operation")

def scalarop(mat):
    choise = int(input("Enter the operation:\n1.add\t2.sub\t3.mul\n4.div\t5.mod\t6.power\n7.floordiv: "))
    num = int(input("Enter number: "))
    match choise:
        case 1:
            return mat+num
        case 2:
            return mat-num
        case 3:
            return mat*num
        case 4:
            return mat/num
        case 5:
            return mat%num
        case 6:
            return mat**num
        case 7:
            return mat//num
def trace(mat):
    trace = 0
    if(mat.shape[0] == mat.shape[1]):
        for i in range(mat.shape[0]):
            trace += mat[i][i]
        print("Matrix trace:",end="\t")
        print(trace)
    else:
        print("unable to perform trace")
def transpose(mat):
    rng = np.random.default_rng()
    mat2 = rng.integers(0,1,size=(mat.shape[1],mat.shape[0]))
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            mat2[j][i] = mat[i][j]
    print(mat2)
def determinant(a):
    if(a.shape[0] == a.shape[1]):
        print("\nMatrix determinant:",end="\t")
        print(np.linalg.det(a))
        return np.linalg.det(a)
    else:
        print("unable to perform operation")
def inverse(a):
    det = determinant(a)
    if((a.shape[0] == a.shape[1]) and (det != 0)):
        print("Inverse matrix:",end="\t")
        print(np.linalg.inv(a))
    else:
        print("inverse does not exist")
def rank(a):
    print("Rank:",end="\t")
    print(np.linalg.matrix_rank(a))



