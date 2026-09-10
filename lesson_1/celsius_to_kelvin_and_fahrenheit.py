def to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 2)

def to_kelvin(celsius):
    return round(celsius + 273.15, 2)

user_celsius = float(input("Введите температуру в Цельсиях: "))
print("Фаренгейт:", to_fahrenheit(user_celsius))
print("Кельвин:", to_kelvin(user_celsius))
