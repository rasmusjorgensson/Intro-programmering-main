import random

val_1 = input("Välj sten, sax eller påse: ")

1 = 'påse'
2 = 'sten'
3 = 'sax'


dator_val = random.randint(1, 3)

print("Du valde", val_1)
print("Datorn valde", dator_val)

if dator_val == val_1:
    print("Oavgjort")

elif val_1 == 'sten' and dator_val == 'sax':
    print("Du vinner!")
elif val_1 == 'sax' and dator_val == 'påse':
    print("Du vinner!")
elif val_1 == 'påse' and dator_val == 'sten':
    print("Du vinner!")

else:
    print("Datorn vinner!")