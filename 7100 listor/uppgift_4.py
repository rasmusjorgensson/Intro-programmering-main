
def caesar_chiffer(text):
    alfabet = list("abcdefghijklmnopqrstuvwxyz")
    chiffrerad_lista = []
    
    for bokstav in text.lower():
        if bokstav in alfabet:
            i = alfabet.index(bokstav)
            ny_i = (i+1) % 26
            chiffrerad_lista.append(alfabet[ny_i])
        else:
            chiffrerad_lista.append(bokstav)

    print("Chiffrerad text:", ''.join(chiffrerad_lista))

text = input("SKriv in ett ord för att chiffrera: ")
caesar_chiffer(text)




