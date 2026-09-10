def bin_kef(num, kef):
    if type(num) is not int or type(kef) is not int:
        raise TypeError("Arguments must be integers.")
    if num < 0 or kef < 0 or kef > num:
        raise ValueError("Invalid values: require 0 ≤ kef ≤ num")

    kef = min(kef, num - kef)

    n = 1
    for i in range(num - kef + 1, num + 1):
        n *= i

    k = 1
    for i in range(1, kef + 1):
        k *= i
    return n // k


user_num = 1000
user_kef = 999
result = bin_kef(user_num, user_kef)
print(f"C({user_num}, {user_kef}) = {result}")