text = input("Vad är din näst sista siffra i ditt personnummer?")
tal = int(text)
if tal % 2 == 0:
    print("Du är en tjej")
else:
    print("Du är en kille")