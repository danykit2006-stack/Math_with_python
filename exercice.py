#Exercice 1
personage1 = "Dan"
score1 = 18
est_en_vie1 = True

personage2 = "Bob"
score2 = 0
est_en_vie2 = False

if score1 > score2:
    personage_gagnant = personage1
    print("Le personnage gagnant est :" + personage_gagnant)
else:
    personage_gagnant = personage2
    print("Le personnage gagnant est :" + personage_gagnant)

#Exercice 2
etudiant1 = "Marck"
moyenne1 = 20
etudiant2 = "John"
moyenne2 = 9
moyenne_minimale = 10

if moyenne1 > moyenne_minimale and moyenne1 == 20:
    print("L'etudiant " + etudiant1 +" est passee avec mention excellente")
elif moyenne2 > moyenne_minimale and moyenne2 == 20:
    print("L'etudiant " + etudiant2 +" est passee avec mention excellente")
elif moyenne1 < moyenne_minimale:
    print("L'etudiant " + etudiant1 +" Rattrapage")
elif moyenne2 < moyenne_minimale:
    print("L'etudiant " + etudiant2 + " Rattrapage")

#Exercice 3
energie = 5
while energie > 0:
    print("saut effectue")
    energie -= 1
#Exercice 4
cours = ["CS101", "MATH200", "HIST3003", "PHYS105"]
cours.append("BIO110")
cours_trie = sorted(cours)
cours_trie.remove("CS101")
print(cours_trie)

#Exercice 5
log_brut = "   erRor: collision_detected   "
log_nettoye = log_brut.strip()
log_nettoye = log_nettoye.replace("_", " ")
print(log_nettoye.capitalize())

#Exercice 6
notes = [14, 16, 12, 18]
def calculer_gpa(notes):
    somme = sum(notes)
    gpa = somme / len(notes)
    return gpa

gpa = calculer_gpa(notes)
print("Le GPA est :", gpa)

#Exercice 7
