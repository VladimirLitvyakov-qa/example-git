def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 25:
        return "Норма, жить можно"
    elif bmi < 30:
        return "Избыточный вес, стоит задуматься"
    else:
        return "Ожирение"

while True:
    input_weight = float(input("Введите ваш вес (кг): "))
    input_height = float(input("Введите ваш рост (м): "))

    if input_weight > 0 and input_height > 0:
        break

    print("Ошибка: Вес и рост должны быть больше нуля! Попробуйте снова.\n")

user_bmi = calculate_bmi(input_weight, input_height)
category = get_bmi_category(user_bmi)

print("Ваш ИМТ: ", round(user_bmi, 1))
print("Категория: ", category)
