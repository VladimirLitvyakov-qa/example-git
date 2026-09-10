def calculate_months_to_threshold(start, rate, threshold) -> int:

    if rate <= 0:
        raise ValueError("Growth rate must be greater than 0.")
    if start <= 0 or threshold <= 0:
        raise ValueError("Start and threshold must be positive numbers.")
    if start >= threshold:
        return 0

    rate_float = rate / 100
    count_month = 0
    count_start = start

    while count_start < threshold:
        count_start = (count_start * rate_float) + count_start
        count_month += 1

    return int(count_month)

while True:
    try:
        user_start = int(input("Введите начальное количество пользователей: "))
        user_rate = float(input("Введите темп роста в процентах: "))
        user_threshold = int(input("Введите пороговое значение: "))

        months = calculate_months_to_threshold(user_start, user_rate, user_threshold)
        print(f"Количество месяцев для достижения порога: {months}")
        break

    except ValueError as error:
        print(f"Ошибка ввода: {error}\nПожалуйста повторите попытку\n")
