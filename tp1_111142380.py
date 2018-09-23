def f(x):
    return x**3 + 1

# Hello
while True:
    n = int(input("Entrez un nombre positif inférieur à 10000 (ou 0 pour terminer): "))
    if n < 0:
        print("Erreur, le nombre doit être positif.")
        print()
        continue
    if n > 10000:
        print("Erreur, le nombre doit être inférieur à 10000.")
        print()
        continue
    if n == 0:              # J'ai choisi d'utiliser break, car on doit
        break               # sortir de la boucle si cette condition est remplie.

    largeur = 1 / n         # À noter que la division retourne un float.
    aire_totale = 0
    for i in range(0, n):
        xg = i * largeur
        xd = xg + largeur   # J'utilise la variable xg au lieu de la recalculer.
        yg = f(xg)
        yd = f(xd)
        hauteur = (yg + yd) / 2
        aire = hauteur * largeur
        aire_totale += aire
    print("Valeur calculée :", aire_totale)
    print("Valeur réelle : 1.25")
    print()
