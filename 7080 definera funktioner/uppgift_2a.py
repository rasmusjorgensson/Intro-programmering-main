def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius +32

celsius = float(input("Skriv in en grad i celsius: "))

print("Ditt tal i fahrenheit är: ", celsius_to_fahrenheit(celsius) )