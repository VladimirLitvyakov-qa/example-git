def summa(number_1, number_2):
    return number_1 + number_2

def difference(number_1, number_2):
    return number_1 - number_2

def composition(number_1, number_2):
    return number_1 * number_2

def division(number_1, number_2):
    try:
        return number_1 / input_number_2
    except ZeroDivisionError:
        return "Деление на ноль запрещено"


input_number_1 = float(input("Введите первое число: "))
input_number_2 = float(input("Введите второе число "))

print("Сумма:", summa(input_number_1, input_number_2))
print("Разность:", difference(input_number_1, input_number_2))
print("Произведение:", composition(input_number_1, input_number_2))
print("Деление:", division(input_number_1, input_number_2))