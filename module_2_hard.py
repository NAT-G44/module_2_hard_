def find_pairs(n):
    result = []
    used_pairs = set()
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            if (a, b) not in used_pairs and n % (a + b) == 0:
                result.append((a, b))
                used_pairs.add((a, b))
                used_pairs.add((b, a))
    result_string = ''.join(f'{a}{b}' for a, b in result)
    return result_string
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = find_pairs(n)
    print("Пароль:", result)
else:
    print("Число должно быть от 3 до 20")


