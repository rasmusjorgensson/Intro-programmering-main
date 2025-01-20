text1 = input("Ange ett tal ")
text2 = input("Ange ett till tal ")
text3 = input("Anget ett tredje tal ")

tal1= input(text1)
tal2= input(text2)
tal3= input(text3)

if tal1 > tal2 and tal3:
    print(tal1,"är större än",tal2,"och",tal3)
elif tal2 > tal1 and tal3:
    print(tal2,"är större än",tal1,"och",tal3)
elif tal3 > tal1 and tal2:
    print(tal3,"är större än",tal1,"och",tal2)