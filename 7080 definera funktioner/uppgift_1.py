def kelvinToCelsius(k):
    return k - 273.15

kelvin_temperature = float(input("Skriv in temperaturen i Kelvin: "))

print("Temperaturen i Celsius är:", kelvinToCelsius(kelvin_temperature))
