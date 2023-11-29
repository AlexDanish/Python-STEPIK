print('Введите 5 пар чисел через пробел')
i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break # досрочно завершаем цикл
    print(a * b)
    i += 1