from calculatrice_logique import evaluer
import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.resizable(False, False)

ecran = tk.Entry(fenetre, font=("Arial", 24), justify="right", bd=8)
ecran.grid(row=0, column=0, columnspan=4, sticky="nsew")


def ajouter(texte):
    ecran.insert(tk.END, texte)


def effacer():
    ecran.delete(0, tk.END)


def calculer():
    expression = ecran.get().strip()
    try:
        if not expression:
            raise ValueError("Expression vide")
        resultat = evaluer(expression)
        # Affiche 14 au lieu de 14.0
        if isinstance(resultat, float) and resultat.is_integer():
            resultat = int(resultat)
    except ZeroDivisionError:
        resultat = "Erreur : division par zéro"
    except ValueError as erreur:
        resultat = f"Erreur : {erreur}"
    effacer()
    ecran.insert(0, str(resultat))


fenetre.bind("<Return>", lambda event: calculer())


touches = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]

for i, t in enumerate(touches):
    if t == "=":
        commande = calculer
    else:
        commande = lambda t=t: ajouter(t)
    tk.Button(fenetre, text=t, font=("Arial", 16), width=5, height=2,
              command=commande).grid(row=1 + i // 4, column=i % 4)

tk.Button(fenetre, text="C", font=("Arial", 16), height=2,
          command=effacer).grid(row=5, column=0, columnspan=4, sticky="nsew")

fenetre.mainloop()