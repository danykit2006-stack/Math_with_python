

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


