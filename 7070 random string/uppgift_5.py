import random

spela = input("Vill du spela? j/n: ")

while spela == 'j':
    tarning1 = random.randint(1, 9)
    tarning2 = random.randint(1, 9)
    tarning3 = random.randint(1, 9)
    print(tarning1, tarning2, tarning3)

    if tarning1 ==  7 and tarning2 == 7 and tarning3 == 7:
        print("Dubbel vinst")
    elif tarning1 == tarning2 == tarning3:
        print("Vinst")
    else:
        print("Förlust")    

    spela = input("Vill du spela igen? j/n: ")

print("Vad roligt att du spelade en stund!")

