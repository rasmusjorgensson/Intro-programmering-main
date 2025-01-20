import random

spela = input("Vill du spela? j/n: ")

while spela == 'j':
    tarning1 = random.randint(1, 6)
    tarning2 = random.randint(1, 6)
    print(tarning1, tarning2)
        
    if tarning1 == tarning2:
        print("vinst")
    else:
        print("förlust")

    spela = input("Vill du spela igen? j/n: ")

print("Vad roligt att du spelade en stund!")

