tal = int(input("Skriv in ett tal: "))

if tal >=0 and tal <= 9 :
    print ("ditt tal är ensiffrigt")
elif tal >=10 and tal <= 99 :
    print ("ditt tal är tvåsiffrigt")
elif tal >=100 and tal <= 999 :
    print ("ditt tal är tresiffrigt")
elif tal >=1000 :
    print("ditt tal är minst fyrsiffrigt")
elif tal < 0:
 print("ditt tal är negativt")

