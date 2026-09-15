try:
    import numpy as np
except ModuleNotFoundError:
    class _NumpyFallback:
        @staticmethod
        def array(data):
            return data

        @staticmethod
        def trace(matrix):
            return sum(matrix[i][i] for i in range(len(matrix)))

        @staticmethod
        def add(a, b):
            return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

        @staticmethod
        def subtract(a, b):
            return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

        @staticmethod
        def dot(a, b):
            return [[sum(a[i][k] * b[k][j] for k in range(len(a))) 
                     for j in range(len(b[0]))] 
                     for i in range(len(a))]

    np = _NumpyFallback()


# ------------------------------
#     MATRIX PRINTING
# ------------------------------

def print_matrix(matrix):
    """Prints a matrix line by line."""
    for row in matrix:
        print(row)


# ------------------------------
#     INPUT UTILITIES
# ------------------------------

def read_matrix(n):
    """Reads an n×n matrix from user input."""
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = float(input(f"Enter element ({i+1},{j+1}): "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)


# ------------------------------
#     MATRIX OPERATIONS
# ------------------------------

def trace_matrix(n):
    matrix = read_matrix(n)
    print("Matrix:")
    print_matrix(matrix)
    return np.trace(matrix)


def add_matrices(n):
    print("Enter first matrix:")
    m1 = read_matrix(n)
    print("Enter second matrix:")
    m2 = read_matrix(n)

    print("First matrix:")
    print_matrix(m1)
    print("Second matrix:")
    print_matrix(m2)

    return np.add(m1, m2)


def subtract_matrices(n):
    print("Enter first matrix:")
    m1 = read_matrix(n)
    print("Enter second matrix:")
    m2 = read_matrix(n)

    print("First matrix:")
    print_matrix(m1)
    print("Second matrix:")
    print_matrix(m2)

    return np.subtract(m1, m2)


def multiply_matrices(n):
    print("Enter first matrix:")
    m1 = read_matrix(n)
    print("Enter second matrix:")
    m2 = read_matrix(n)

    print("First matrix:")
    print_matrix(m1)
    print("Second matrix:")
    print_matrix(m2)

    return np.dot(m1, m2)


# ------------------------------
#     MENU
# ------------------------------

def main():
    print("Matrix Calculator")
    print("1. Trace")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Multiplication")

    choice = int(input("Choose an operation: "))
    size = int(input("Matrix size (2 or 3): "))

    if choice == 1:
        result = trace_matrix(size)
    elif choice == 2:
        result = add_matrices(size)
    elif choice == 3:
        result = subtract_matrices(size)
    elif choice == 4:
        result = multiply_matrices(size)
    else:
        print("Invalid choice.")
        return

    print("Result:")
    print_matrix(result)


if __name__ == "__main__":
    main()
