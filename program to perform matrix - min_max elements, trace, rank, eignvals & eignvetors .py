'''
install python3
pip install numpy

###########################################################
Code 2:
Write a Program to perform the following operations
1) Find the minimum and maximum element of the matrix
2) Find the minimum and maximum element of each row in the matrix
3) Find the minimum and maximum element of each column in the matrix
4) Find trace of the given matrix
5) Find rank of the given matrix
6) Find eigenvalues and eigenvectors of the given matrix
###########################################################
'''

import numpy as np

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter the element at position {i+1}, {j+1} :"))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

def find_min_max(matrix):
    min_elements = np.min(matrix)
    max_elements = np.max(matrix)
    return min_elements, max_elements

def find_min_max_row(matrix):
    min_elements = np.min(matrix, axis=1)
    max_elements = np.max(matrix, axis=1)
    return min_elements, max_elements

def find_min_max_cols(matrix):
    min_elements = np.min(matrix, axis=0)
    max_elements = np.max(matrix, axis=0)
    return min_elements, max_elements

def find_trace(matrix):
    return np.trace(matrix)

def find_rank(matrix):
    return np.linalg.matrix_rank(matrix)

def find_eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

if __name__ == "__main__":

    rows = int(input("Enter the number of rows for the Matrix: "))
    cols = int(input("Enter the number of columns for the Matrix: "))
    matrix = input_matrix(rows, cols)

    print("Matrix:")
    print(matrix)

    min_elements, max_elements = find_min_max(matrix)
    print("Minimum Element of the matrix: ", min_elements)
    print("Maximun Element of the Matrix: ", max_elements)

    min_elements_row, max_elements_row = find_min_max_row(matrix)
    print("Minimum Element of Each Row: ", min_elements_row)
    print("Maximun Element of Each Row: ", max_elements_row)

    min_elements_cols, max_elements_cols = find_min_max_cols(matrix)
    print("Minimum Element of Each Column: ", min_elements_cols)
    print("Maximun Element of Each Column: ", max_elements_cols)

    trace = find_trace(matrix)
    print("Trace of the Matrix:", trace)

    rank = find_rank(matrix)
    print("Rank of the Matrix:", rank)

    eigenvalues, eigenvectors = find_eigen(matrix)
    print("Eigenvalues:")
    print(eigenvalues)
    print("Eigenvectors: ")
    print(eigenvectors)
        
