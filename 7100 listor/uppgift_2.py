primtal = []

for tal in range(2, 100):
    for i in range(2, tal):
        if tal % i == 0:
            break
    else:
        primtal.append(tal)

print("Primtal under 100:", primtal)

