import random

tarningar = [random.randint(1,6) for i in range (5)]

tarningar.sort()

antal_ettor = tarningar.count(1)


print(antal_ettor, tarningar)
