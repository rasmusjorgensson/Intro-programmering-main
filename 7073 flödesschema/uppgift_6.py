antal_gissningar = 0
tal = int(input("Gissa ett tal: "))


while tal != 42:
    antal_gissningar += 1  
    if tal < 42:
        print("För litet")
    elif tal > 42:
        print("För stort")
    
    tal = int(input("Gissa igen: "))

antal_gissningar += 1  
print("Du behövde", antal_gissningar , " gissningar för att hitta rätt svar.")
