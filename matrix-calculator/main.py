import numpy as np
import matrix_op
print("WELCOME...\n")
print("Menu\n")
a = 0
b = 0
while True:
    print("1.Create matrix (A)\n2.Create matrix (b)\n3.Matrix addition(A+B)\n4.Matrix substraction(A-B)\n5.Matrix multiplication(A@B)\n6.Scalar operations\n7.Transpose matrix\n8.Trace of matrix\n9.Determinant\n10.Inverse\n11.Rank\n12.Exit")
    try:
        choice = int(input("Enter the corresponding integer: "))
    except:
        print("Enter a valid integer")
    match choice:
        case 1:
            a = matrix_op.create()
        case 2:
            b = matrix_op.create()
        case 3:
            try:
                matrix_op.add(a,b)
            except:
                print("Error: did you created matrix A and B??")
        case 4:
            try:
                matrix_op.sub(a,b)
            except:
                print("Error: did you created matrix A and B??")
        case 5:
            try:
                matrix_op.matmul(a,b)
            except:
                print("Error: did you created matrix A and B??")
        case 6:
            matrix = input("Enter the matrix you want to perform operations on: ").lower()
            if(matrix == "a"):
                mat = matrix_op.scalarop(a)
                print(mat)
            elif(matrix == "b"):
                mat = matrix_op.scalarop(b)
                print(mat)
            else:
                print("Enter a valid matrix")
        case 7:
            matrix = input("Enter the matrix you want to perform operations on: ").lower()
            if(matrix == "a"):
                mat = matrix_op.transpose(a)
                print(mat)
            elif(matrix == "b"):
                mat = matrix_op.transpose(b)
                print(mat)
            else:
                print("Enter a valid matrix")
        case 8:
            matrix = input("Enter the matrix you want to perform operations on: ").lower()
            if(matrix == "a"):
                mat = matrix_op.trace(a)
                print(mat)
            elif(matrix == "b"):
                mat = matrix_op.trace(b)
                print(mat)
            else:
                print("Enter a valid matrix")
        case 9:
            matrix = input("Enter the matrix you want to perform operations on: ").lower()
            if(matrix == "a"):
                mat = matrix_op.determinant(a)
                print(mat)
            elif(matrix == "b"):
                mat = matrix_op.determinant(b)
                print(mat)
            else:
                print("Enter a valid matrix")
        case 10:
            matrix = input("Enter the matrix you want to perform operations on: ").lower()
            if(matrix == "a"):
                mat = matrix_op.inverse(a)
                print(mat)
            elif(matrix == "b"):
                mat = matrix_op.inverse(b)
                print(mat)
            else:
                print("Enter a valid matrix")
        case 11:
            matrix = input("Enter the matrix you want to perform operations on: ").lower()
            if(matrix == "a"):
                mat = matrix_op.rank(a)
                print(mat)
            elif(matrix == "b"):
                mat = matrix_op.rank(b)
                print(mat)
            else:
                print("Enter a valid matrix")
        case 12:
            print("Thankyou...")
            break