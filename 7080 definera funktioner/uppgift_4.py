def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius +32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)/(9/5)
def kelvin_to_celsius(kelvin):
     return kelvin - 273.15
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    while True:
        print("Välj en omvandling")
        print("1. Celsius till Fahrenheit: ")
        print("2. Fahrenheit till Celsius: ")
        print("3. Kelvin till Celsius: ")
        print("4. Celsius till Kelvin: ")
        print("5. Fahrenheit till Kelvin: ")
        print("6. Kelvin till Fahrenheit: ")
        print("7. Avsluta")

        val = input("Ange vilken du vill omvandla (1-7): ")
        if val == '7':
            print("Avslutar")
            break

        temperatur = float(input("Skriv temperaturen: "))

        if val == '1':
            print(temperatur, "Celsius är: ", celsius_to_fahrenheit(temperatur), "Fahrenheit")
        elif val == '2':
            print(temperatur, "Fahrenheit är: ", fahrenheit_to_celsius(temperatur), "Celsius")
        elif val == '3':
            print(temperatur, "Kelvin är: ", kelvin_to_celsius(temperatur), "Celsius")
        elif val == '4':
            print(temperatur, "Celsius är: ", celsius_to_kelvin(temperatur), "Kelvin")
        elif val == '5':
            print(temperatur, "Fahrenheit är: ", fahrenheit_to_kelvin(temperatur), "Kelvin")
        elif val == '6':
            print(temperatur, "Kelvin är: ", kelvin_to_fahrenheit(temperatur), "Fahrenheit")
        else:
            print("Välj ett tal 1-7.")


main()