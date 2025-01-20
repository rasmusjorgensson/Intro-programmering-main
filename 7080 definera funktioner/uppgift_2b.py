def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)/(9/5)

fahrenheit = float(input("Skriv en grad i fahrenheit: "))
print("Din grad i celsius är:", fahrenheit_to_celsius(fahrenheit))