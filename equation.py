

#This program calculates the roots of the linear equation of the form ax + b = 0
def equation_linear():
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
def equation_second_degree():
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
def equation_rational():
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

#This program calculate the roots of irational equation of the form root^2(ax + b) = c
def equation_irational():
    coefficient1 = float(input("Entrer le coefficient de x du radical: "))
    coefficient2 = float(input("Entrer le coefficient du term independant du radical: "))
    coefficient3 = float(input("Entrer le coefficient du term independant hors radical: "))
    a = coefficient1
    b = coefficient2
    c = coefficient3
    sup_radical = c**2
    c = sup_radical
    solve = (c - b) / a 
    return f"La solution de l'equation est : {solve}"

#This is the main menu.
def main():
    while True:
        print("\nEquation calculator.")
        print("1.Equation lineaire(ax + b = 0).")
        print("2.Equation du second degree(ax^2 + bx + c = 0).")
        print("3.Equation rationnel(ax + b) / (cx + d) = 0.")
        print("4.Equation irrationnel √(ax + b) = 0.")
        print("5.Quitter.")

        choice = int(input("Choisissez une option : "))

        if choice == 1:
            print(equation_linear())
            continue

        if choice == 2:
            print(equation_second_degree())
            continue

        if choice == 3:
            print(equation_rational())
            continue

        if choice == 4:
            print(equation_irational())
            continue

        if choice == 5:
            print("Programme terminer ! ")
            break

        print("Choix invalide !")

if __name__ == "__main__":
    main()






