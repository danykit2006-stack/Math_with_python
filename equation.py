import numpy as np
# This program calculates the roots of a second-degree equation of the form ax² + bx + c = 0
coefficient1 = float(input("Enter the coefficient of x²: "))
coefficient2 = float(input("Enter the coefficient of x: "))
term_constant = float(input("Enter the constant term: "))

def equation_second_degree(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = (-b + delta**0.5) / (2*a)
        root2 = (-b - delta**0.5) / (2*a)
        return f"The solution of the equation is: x1 = {root1} and x2 = {root2}"
    elif delta == 0:
        root = -b / (2*a)
        return f"The solution of the equation is: x = {root}"
    else:
        return "The equation has no real solution."
    
print(equation_second_degree(coefficient1, coefficient2, term_constant))

#This program checks the collinearity of two 2D vectors (x, y).
vector1 = [float(input("Enter the x component of the first vector: ")), float(input("Enter the y component of the first vector: "))]
vector2 = [float(input("Enter the x component of the second vector: ")), float(input("Enter the y component of the second vector: "))]

def check_collinearity(v1, v2):
    if v1[0] * v2[1] == v1[1] * v2[0]:
        return "The vectors are collinear."
    else:
        return "The vectors are not collinear."

print(check_collinearity(vector1, vector2))

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

