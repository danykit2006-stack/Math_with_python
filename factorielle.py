
#This program calculate the factoriel of number
def factoriel():
    n = int(input("Entrer un entier naturel : "))
    fact = 1

    for n in range(2, n+1):
        fact *= n

    print(f"Le factoriel de {n} est {fact}")

factoriel()
