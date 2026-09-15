try:
    import numpy as np
except ModuleNotFoundError:
    class _NumpyFallback:
        @staticmethod
        def array(data):
            return data

        @staticmethod
        def trace(matrix):
            return sum(matrix[i][i] for i in range(min(len(matrix), len(matrix[0]))))

    np = _NumpyFallback()


#This is a program for the trace of a 2x2 matrix.
def trace_matrix(matrix):
    matrix = np.array([[float(input("Enter the element at position (1,1): ")), float(input("Enter the element at position (1,2): "))],
                   [float(input("Enter the element at position (2,1): ")), float(input("Enter the element at position (2,2): "))]])
    print(f"The matrix is:\n{matrix}")
    return np.trace(matrix)

#This is a program for the trace of a 3x3 matrix.
def trace_matrix_3x3(matrix):
    matrix = np.array([[float(input("Enter the element at position (1,1): ")), float(input("Enter the element at position (1,2): ")), float(input("Enter the element at position (1,3): "))],
                   [float(input("Enter the element at position (2,1): ")), float(input("Enter the element at position (2,2): ")), float(input("Enter the element at position (2,3): "))],
                   [float(input("Enter the element at position (3,1): ")), float(input("Enter the element at position (3,2): ")), float(input("Enter the element at position (3,3): "))]])
    print(f"The matrix is:\n{matrix}")
    return np.trace(matrix)

#This program addition of two 2x2 matrices.
def add_matrices(matrix1, matrix2):
    matrix1 = np.array([[float(input("Enter the element at position (1,1) of the first matrix: ")), float(input("Enter the element at position (1,2) of the first matrix: "))],
                   [float(input("Enter the element at position (2,1) of the first matrix: ")), float(input("Enter the element at position (2,2) of the first matrix: "))]])
    matrix2 = np.array([[float(input("Enter the element at position (1,1) of the second matrix: ")), float(input("Enter the element at position (1,2) of the second matrix: "))],
                   [float(input("Enter the element at position (2,1) of the second matrix: ")), float(input("Enter the element at position (2,2) of the second matrix: "))]])
    print(f"The first matrix is:\n{matrix1}")
    print(f"The second matrix is:\n{matrix2}")
    return np.add(matrix1, matrix2)

#This program addition of two 3x3 matrix.
def add_matrices_3x3(matrix1, matrix2):
    matrix1 = np.array([[float(input("Enter the element at position (1,1) of the first matrix: ")), float(input("Enter the element at position (1,2) of the first matrix: ")), float(input("Enter the element at position (1,3) of the first matrix: "))],
                   [float(input("Enter the element at position (2,1) of the first matrix: ")), float(input("Enter the element at position (2,2) of the first matrix: ")), float(input("Enter the element at position (2,3) of the first matrix: "))],
                   [float(input("Enter the element at position (3,1) of the first matrix: ")), float(input("Enter the element at position (3,2) of the first matrix: ")), float(input("Enter the element at position (3,3) of the first matrix: "))]])
    matrix2 = np.array([[float(input("Enter the element at position (1,1) of the second matrix: ")), float(input("Enter the element at position (1,2) of the second matrix: ")), float(input("Enter the element at position (1,3) of the second matrix: "))],
                   [float(input("Enter the element at position (2,1) of the second matrix: ")), float(input("Enter the element at position (2,2) of the second matrix: ")), float(input("Enter the element at position (2,3) of the second matrix: "))],
                   [float(input("Enter the element at position (3,1) of the second matrix: ")), float(input("Enter the element at position (3,2) of the second matrix: ")), float(input("Enter the element at position (3,3) of the second matrix: "))]])
    print(f"The first matrix is:\n{matrix1}")
    print(f"The second matrix is:\n{matrix2}")
    return np.add(matrix1, matrix2)

#This program subtraction of two 2x2 matrices.
def subtract_matrices(matrix1, matrix2):
    matrix1 = np.array([[float(input("Enter the element at position (1,1) of the first matrix: ")), float(input("Enter the element at position (1,2) of the first matrix: "))],
                   [float(input("Enter the element at position (2,1) of the first matrix: ")), float(input("Enter the element at position (2,2) of the first matrix: "))]])
    matrix2 = np.array([[float(input("Enter the element at position (1,1) of the second matrix: ")), float(input("Enter the element at position (1,2) of the second matrix: "))],
                   [float(input("Enter the element at position (2,1) of the second matrix: ")), float(input("Enter the element at position (2,2) of the second matrix: "))]])
    print(f"The first matrix is:\n{matrix1}")
    print(f"The second matrix is:\n{matrix2}")
    return np.subtract(matrix1, matrix2)    