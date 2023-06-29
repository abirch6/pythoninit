liste_nombres = [1, 2, 3, 4, 5]
liste_chaines = ["apple", "banane", "orange"]
liste_mixte = [10, "hello", True, 3.14]
print(liste_nombres[0])
print(liste_chaines[2])
print(liste_mixte[1])

liste_nombres[2] = 100
print(liste_nombres)

liste_chaines.append("grape")
print(liste_chaines)

del liste_mixte[0]
print(liste_mixte)

liste_nombres.reverse()
print(liste_nombres)

