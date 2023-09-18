# Ввод данных
x1, y1, a1, b1, x2, y2 = map(int, input().split())

# Вычисляем разницу между текущим временем и правильным временем
time_difference = (x2 - x1) * 60 + (y2 - y1)

# Делим разницу на два, так как часы идут вдвое медленнее
time_difference //= 2

# Добавляем разницу к текущему времени
a2 = a1 + time_difference // 60
b2 = b1 + time_difference % 60

# Проверяем, чтобы минуты были в пределах от 0 до 59
if b2 >= 60:
    a2 += 1
    b2 -= 60

# Проверяем, чтобы часы были в пределах от 0 до 23
a2 %= 24

# Выводим результат
print(a2, b2)