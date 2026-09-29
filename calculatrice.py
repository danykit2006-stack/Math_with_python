#Perimetre d'operation
chiffres = "0123456789"
operateur = "+-*/"
effacer = "c"
egal = "="
virgule = "."

#
def convertir(texte):
    try:
        return float(texte)
    except ValueError:
        raise ValueError("Saisie incorrecte")


#Pour le operation de base(+, -, /, *)
def calculer(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division par zero")
        return a / b
    raise ValueError(f"Operation iconnu : {op} ")

#Test console
if __name__ == "__main__":
    while True:
        try:
            a = convertir(input("Premier nombre : "))
            op = input("Operateur (+ - * /) : ")
            b = convertir(input("Deuxieme nombre : "))
            print("Resultat : ", calculer(a, b, op))
        except (ValueError, ZeroDivisionError) as e:
            print("Erreur :", e)    
