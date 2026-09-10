def decimal_to_binary(num):
    if type(num) is not int:
        raise TypeError("Input must be an integer.")
    if num < 0:
        raise ValueError("Only non-negative integers are allowed.")

    c = ""
    while True:
        c += str(num % 2)
        num = num // 2
        if num == 0:
            break
    return c[::-1]

user_num = True
binary = decimal_to_binary(user_num)
print(f"Двоичное представление: {binary}")
