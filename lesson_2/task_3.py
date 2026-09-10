def how_many_times(message):
    if not isinstance(message, str):
        raise TypeError(f"Ожидалась строка, получено: {type(message).__name__}")

    count = 0
    for i in message.lower().replace(" ", ""):
        if  97 <= ord(i) <= 122:
            count += ord(i) - ord('a') + 1
        else:
            raise ValueError(f"Символ {i} не входит в диапазон 'a'-'z'")
    return count

user_message = input("Введите сообщение (строчные буквы): ")
clicks = how_many_times(user_message)
