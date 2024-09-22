def find_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f"{i}{j}"
    return result
import random
num = random.randint(3, 20)
result = find_password(num)
print("Пароль для числа", num, ":", result)