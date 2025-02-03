def är_jämnt(tal):
    return tal % 2 == 0


nummer = int(input("Ange ett heltal: "))
if är_jämnt(nummer):
    print(nummer, "är ett jämnt tal.")
else:
    print(nummer, "är ett udda tal.")
