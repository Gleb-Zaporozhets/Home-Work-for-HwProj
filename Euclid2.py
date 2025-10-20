def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида.
    Возвращает кортеж (g, x, y), где g = gcd(a, b),
    а также такие x и y, что a*x + b*y = g.
    """
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (g, x, y)

# Пример использования:
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

g, x, y = extended_gcd(a, b)

print(f"НОД({a}, {b}) = {g}")
print(f"Рассмотрение соотношения Безу: {a}*({x}) + {b}*({y}) = {g}")