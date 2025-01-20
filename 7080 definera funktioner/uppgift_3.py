def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

kelvin= float(input("Skriv in en grad i kelvin: "))
print("Din grad i fahrenheit är: ", kelvin_to_fahrenheit(kelvin))