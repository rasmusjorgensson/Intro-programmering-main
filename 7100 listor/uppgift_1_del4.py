import random
tal = [random.randint(0, 2) for i in range(12)]

for i in range(len(tal)):
    if tal[i] == 0:
        tal[i] = 3

print(tal)
