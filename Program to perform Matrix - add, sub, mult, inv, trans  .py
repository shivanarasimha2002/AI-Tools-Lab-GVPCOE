'''
install python3
pip install numpy
-----------------------------------------------------------------------------------
##################################################
Code 1:
Write a Program to perform the following operations on matrices
1) Matrix addition
2) Matrix Subtraction
3) Matrix Multiplication
4) Matrix Inversion
5) Transpose of a Matrix
####################################################
'''

import numpy as np

def input_matrix(rows,cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter the element at position {i+1}, {j+1}"))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)    

def matrix_add(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def matrix_sub(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def matrix_mult(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def matrix_inverse(matrix):
    return np.linalg.inv(matrix)

def matrix_transpose(matrix):
    return matrix.T

if __name__ == "__main__":

    rows1 = int(input("Enter the number of rows for the Matrix 1: "))
    cols1 = int(input("Enter the number of columns for the Matrix 1: "))
    matrix1 = input_matrix(rows1,cols1)

    rows2 = int(input("Enter the number of rows for the Matrix 2: "))
    cols2 = int(input("Enter the number of columns for the Matrix 2: "))
    matrix2 = input_matrix(rows2,cols2)

    result_add = matrix_add(matrix1, matrix2)
    print("Matrix Addition: ")
    print(result_add)

    result_sub = matrix_sub(matrix1, matrix2)
    print("Matrix Subtraction: ")
    print(result_sub)

    try:
        result_mult = matrix_mult(matrix1, matrix2)
        print("Matrix Multiplication: ")
        print(result_mult)
    except ValueError as e:
        print("Matrix multiplicagtion cannot be performed\n Make sure the number of columns in Matrix1 is equal to the number of rows in Matrix2")

    print("Matrix Transpose (Matrix 1): ")
    print(matrix_transpose(matrix1)) 
    print("Matrix Transpose (Matrix 2): ")
    print(matrix_transpose(matrix2)) 

    try:
        inverse_matrix1 = matrix_inverse(matrix1)
        inverse_matrix2 = matrix_inverse(matrix2)
        print("Matrix Inverse (Matrix 1): ")
        print(inverse_matrix1)
        print("Matrix Inverse (Matrix 2): ")
        print(inverse_matrix2)
    except np.linalg.LinAlgError as e:
        print("Matrix is not invertible")

