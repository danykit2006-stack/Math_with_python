import ast
import operator

#operateur(+ - * /)
OPERATEURS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

def evaluer(expression):
    try:
        arbre = ast.parse(expression, mode="eval")
    except SyntaxError:
        raise ValueError("Expression incorrecte")
    return _eval(arbre.body)


def _eval(noeud):
    #Un nombre
    if isinstance(noeud, ast.Constant) and isinstance(noeud.value, (int, float)):
        return noeud.value
    #Un nombre negatif
    if isinstance(noeud, ast.UnaryOp) and isinstance(noeud.op, (ast.USub, ast.UAdd)):
        val = _eval(noeud.operand)
        return -val if isinstance(noeud.op, ast.USub) else val
    #Une operation (+ - * /)
    if isinstance(noeud, ast.BinOp) and type(noeud.op) in OPERATEURS:
        gauche = _eval(noeud.left)
        droite = _eval(noeud.right)
        if isinstance(noeud.op, ast.Div) and droite == 0:
            raise ZeroDivisionError("Division par zero")
        return OPERATEURS[type(noeud.op)](gauche, droite)
    raise ValueError("Expression non autorisee")
    

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
            print("Résultat :", evaluer(input("Expression : ")))
        except (ValueError, ZeroDivisionError) as e:
            print("Erreur :", e)
