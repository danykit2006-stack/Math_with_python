
#This program checks the collinearity of two 2D vectors (x, y).
vector1 = [float(input("Enter the x component of the first vector: ")), float(input("Enter the y component of the first vector: "))]
vector2 = [float(input("Enter the x component of the second vector: ")), float(input("Enter the y component of the second vector: "))]

def check_collinearity(v1, v2):
    if v1[0] * v2[1] == v1[1] * v2[0]:
        return "The vectors are collinear."
    else:
        return "The vectors are not collinear."
print(check_collinearity(vector1, vector2))
