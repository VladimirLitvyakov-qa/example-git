def discriminant(a, b, c):
    return b ** 2 - 4 * a * c

def solve_quadratic(a, b, c):
    d = discriminant(a, b, c)

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif d == 0:
        x = -b / (2 * a)
        return round(x, 2)
    else:
        real = -b / (2 * a)
        imag = (abs(d) ** 0.5) / (2 * a)
        x1 = complex(round(real, 2), round(imag, 2))
        x2 = complex(round(real, 2), -round(imag, 2))
        return x1, x2

while True:
    aa = float(input("Введите коэффициент a: "))
    if aa == 0:
        print("Коэффициент a не может равен нулю в квадратном уравнении!")
    else:
        break

bb = float(input("Введите коэффициент b: "))
cc = float(input("Введите коэффициент c: "))

roots = solve_quadratic(aa, bb, cc)
print("Корни уравнения:", roots)