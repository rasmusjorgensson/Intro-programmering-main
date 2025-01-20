import random
print("Hej och välkommen till tärningspelet")
kassa = 100

vill_spela = "ja"
while vill_spela == 'ja':
    tarning_1 = random.randint(1, 6)
    tarning_2 = random.randint(1, 6)
    print(tarning_1 + tarning_2)

    if tarning_1 == tarning_2:
        kassa=kassa + tarning_1 + tarning_2
        print("Vinst, kassa =", kassa)
    else:
        kassa - tarning_1 - tarning_2
        print("förlust, kassa = ", kassa)

    vill_spela = input("Vill du spela igen? ja eller nej ")
    if vill_spela == 'nej':
        print("Tack för att du ville spela")
