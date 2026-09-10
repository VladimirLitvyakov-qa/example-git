def armstrong_num(num: int):
    """
    Функция находит и печатает все числа Армстронга в диапазоне от 1 до num.
    :param num: Целое неотрицательно число
    """
    if type(num) is not int:
       raise TypeError("Input must be an integer")
    if num == 0:
       return
    if num < 0:
       raise ValueError("Input must be non-negative")

    for i in range(1, num + 1):
        temp = i
        digit_count = 0
        while temp > 0:
            temp //= 10
            digit_count += 1

        temp = i
        digit_summ = 0
        while temp > 0:
            digit_summ += (temp % 10) ** digit_count
            temp //= 10

        if digit_summ == i:
            if i == 1:
                print(i, end="")
            else:
                print(", ", end="")
                print(i, end="")

armstrong_num(3333)
