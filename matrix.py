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

        @staticmethod
        def det(matrix):
            # Déterminant 2x2
            if len(matrix) == 2:
                return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
            # Déterminant 3x3
            if len(matrix) == 3:
                a,b,c = matrix[0]
                d,e,f = matrix[1]
                g,h,i = matrix[2]
                return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
            raise ValueError("Determinant only supports 2x2 or 3x3.")

        @staticmethod
        def inv(matrix):
            det = _NumpyFallback.det(matrix)
            if det == 0:
                raise ValueError("Matrix is not invertible (det = 0).")

            if len(matrix) == 2:
                a,b = matrix[0]
                c,d = matrix[1]
                return [[ d/det, -b/det],
                        [-c/det,  a/det]]

            if len(matrix) == 3:
                # Inversion 3x3 (méthode des cofacteurs)
                import copy
                m = matrix
                cof = [[0]*3 for _ in range(3)]
                for i in range(3):
                    for j in range(3):
                        sub = [row[:j] + row[j+1:] for k,row in enumerate(m) if k != i]
                        cof[i][j] = ((-1)**(i+j)) * _NumpyFallback.det(sub)
                # Transposée des cofacteurs / det
                return [[cof[j][i]/det for j in range(3)] for i in range(3)]

            raise ValueError("Inverse only supports 2x2 or 3x3.")

    np = _NumpyFallback()


# ------------------------------
#     MATRIX PRINTING
# ------------------------------

def print_matrix(matrix):
    for row in matrix:
        print(row)


# ------------------------------
#     INPUT UTILITIES
# ------------------------------

def read_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = float(input(f"Enter element ({i+1},{j+1}): "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)


# ------------------------------
#     MAIN LOGIC
# ------------------------------

def main():
    stored_matrix = None

    while True:
        print("\nMatrix Calculator")
        print("1. Tracer une matrice")
        print("2. Addition")
        print("3. Soustraction")
        print("4. Multiplication")
        print("5. Déterminant")
        print("6. Inversion")
        print("7. Trace")
        print("8. Puissance")
        print("9. Multiplication par un nombre")
        print("10. Quitter")

        choice = int(input("Choisissez une option : "))

        # OPTION 1 : TRACER UNE MATRICE
        if choice == 1:
            size = int(input("Taille de la matrice (2 ou 3) : "))
            stored_matrix = read_matrix(size)
            print("Matrice tracée :")
            print_matrix(stored_matrix)
            continue

        # Vérification : matrice obligatoire
        if stored_matrix is None and choice != 10:
            print("Vous devez d'abord tracer une matrice (option 1).")
            continue

        # OPTION 2 : ADDITION
        if choice == 2:
            print("Tracez une deuxième matrice :")
            m2 = read_matrix(len(stored_matrix))
            result = np.add(stored_matrix, m2)
            print("Résultat :")
            print_matrix(result)
            stored_matrix = None
            continue

        # OPTION 3 : SOUSTRACTION
        if choice == 3:
            print("Tracez une deuxième matrice :")
            m2 = read_matrix(len(stored_matrix))
            result = np.subtract(stored_matrix, m2)
            print("Résultat :")
            print_matrix(result)
            stored_matrix = None
            continue

        # OPTION 4 : MULTIPLICATION
        if choice == 4:
            print("Tracez une deuxième matrice :")
            m2 = read_matrix(len(stored_matrix))
            result = np.dot(stored_matrix, m2)
            print("Résultat :")
            print_matrix(result)
            stored_matrix = None
            continue

        # OPTION 5 : DÉTERMINANT
        if choice == 5:
            det = np.det(stored_matrix)
            print("Déterminant :", det)
            continue

        # OPTION 6 : INVERSION
        if choice == 6:
            det = np.det(stored_matrix)
            if det == 0:
                print("La matrice n'est pas inversible (det = 0).")
            else:
                inv = np.inv(stored_matrix)
                print("Inverse :")
                print_matrix(inv)
            continue

        # OPTION 7 : TRACE
        if choice == 7:
            tr = np.trace(stored_matrix)
            print("Trace :", tr)
            continue

        # OPTION 8 : PUISSANCE
        if choice == 8:
            p = int(input("Puissance : "))
            result = stored_matrix
            for _ in range(p-1):
                result = np.dot(result, stored_matrix)
            print("Résultat :")
            print_matrix(result)
            continue

        # OPTION 9 : MULTIPLICATION PAR UN NOMBRE
        if choice == 9:
            k = float(input("Entrez le nombre : "))
            result = [[k * x for x in row] for row in stored_matrix]
            print("Résultat :")
            print_matrix(result)
            continue

        # OPTION 10 : QUITTER
        if choice == 10:
            print("Programme terminé.")
            break

        print("Choix invalide.")
