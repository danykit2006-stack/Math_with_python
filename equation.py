

#This program calculates the roots of the linear equation of the form ax + b = 0
def equation_linear(a, b):
    coefficient = float(input("Enter le coefficient de x: "))
    term_constant = float(input("Enter le terme constant: "))
    a = coefficient
    b = term_constant
    if a == 0:
        if b == 0:
            return "L'équation a une infinité de solutions."
        else:
            return "L'équation n'a pas de solution."
    else:
        return f"La solution de l'équation est: x = {-b/a}"

# This program calculates the roots of a second-degree equation of the form ax² + bx + c = 0
def equation_second_degree(a, b, c):
    coefficient1 = float(input("Enter le coefficient de x²: "))
    coefficient2 = float(input("Enter le coefficient de x: "))
    term_constant = float(input("Enter le terme constant: "))
    a = coefficient1
    b = coefficient2
    c = term_constant
    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = (-b + delta**0.5) / (2*a)
        root2 = (-b - delta**0.5) / (2*a)
        return f"La solution de l'équation est: x1 = {root1} and x2 = {root2}"
    elif delta == 0:
        root = -b / (2*a)
        return f"La solution de l'équation est: x = {root}"
    else:
        return "L'équation n'a pas de solution réelle."
       
#This program calculates the roots of rational equations of the form (ax + b) / (cx + d) = 0
def equation_rational(a, b, c, d):
    coefficient1 = float(input("Enter le coefficient de x du numérateur: "))
    term_constant1 = float(input("Enter le terme constant du numérateur: "))
    coefficient2 = float(input("Enter le coefficient de x du dénominateur: "))
    term_constant2 = float(input("Enter le terme constant du dénominateur: "))
    a = coefficient1
    b = term_constant1
    c = coefficient2
    d = term_constant2
    if c == 0:
        if d == 0:
            return "L'équation n'a pas de solution."
        else:
            return f"La solution de l'équation est: x = {-b/a}"
    else:
        return f"La solution de l'équation est: x = {-b/a} and x ≠ {-d/c}"

