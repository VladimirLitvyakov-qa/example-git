"""
Исключения и особые случаи:
- Если хотя бы одна сторона ≤ 0 — результат "Невозможно" (треугольник не существует)
- Проверка возможности построения треугольника по неравенству треугольника:
  - a + b > c, a + c > b, b + c > a
  - если это не выполняется — вернуть "Невозможно"

Ограничения:
- Входные значения — положительные числа
- Не использовать сторонние библиотеки
- Сравнение выполняется строго: >, а не >=
"""


def triangle_type(a, b, c):

    if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (int, float):
        raise TypeError("Input must be an integer or float")

    if (a + b > c and a + c > b and b + c > a) and a > 0 and b > 0 and c > 0:
        if a == b == c:
            return "Равносторонний"
        elif a != b and a != c and b != c:
            return "Разносторонний"
        else:
            return "Равнобедренный"
    else:
        return "Невозможно"

print(triangle_type(5, 5, 5))