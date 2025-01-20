import random

tarningar = [random.randint(1, 6) for i in range(10)]

tarningar.sort()

antal_tarningar = len(tarningar)

summan = sum(tarningar)

medel = sum(tarningar)/len(tarningar)

minsta = min(tarningar)

storsta = max(tarningar)

sexor = tarningar.count(6)

valor = max(set(tarningar), key=tarningar.count)

print("antal tärningar kastade: ", antal_tarningar)
print("summan: ", summan)
print("medelvärde: ", medel)
print("minsta värde: ", minsta)
print("största värde: ", storsta)
print("antal sexor: ", sexor)
print("Vanligaste valören: ", valor)


