text = input("Skriv ett nummer ")
tal = int(text)

if tal >=0 and tal <= 9 :
    print ("ditt tal är ensiffrigt")
if tal >=10 and tal <= 99 :
    print ("ditt tal är tvåsiffrigt")
if tal >=100 and tal <= 999 :
    print ("ditt tal är tresiffrigt")
if tal < 0 :
    print ("ditt tal är negativt")