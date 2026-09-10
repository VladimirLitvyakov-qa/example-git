def tribonacci(n):
    a, b, c = 0, 1, 1

    if type(n) is not int:
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n <= 2:
        return 1
    else:
        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c
    return c

result = tribonacci(10)
print(result)
