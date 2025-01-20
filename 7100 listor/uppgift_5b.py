import random

tarningar = [random.randint(1, 6) for i in range(5)]

if all(tal == tarningar[0] for tal in tarningar):
    resultat = "Yatzy"
else:
    resultat = "Inte yatzy"

print("Tärningarna:", tarningar)
print(resultat)
