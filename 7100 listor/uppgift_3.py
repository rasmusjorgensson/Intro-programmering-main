ord = input("Mata in ett ord att översätta till rövarspråket: ")
vokaler = "aeiouåäöAEIOUÅÄÖ"
resultat = []

for bokstav in ord:
    if bokstav in vokaler:
        resultat.append(bokstav)  
    else:
        resultat.append(bokstav + 'o' + bokstav.lower())

rovarord = "".join(resultat)
print("Ditt ord i rövarspråk blir: ", rovarord)
