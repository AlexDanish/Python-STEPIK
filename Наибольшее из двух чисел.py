print('Деление двух чисел')
print('Введите первое число')
a = int(input())
print('Введите второе число')
b = int(input())
if b != 0:
    print(a / b)
else:
    print('Деление невозможно')
    b = int(input('Введите ненулевое значение '))
    if b == 0:
        print('Вы не справились!')
    else:
        print(a / b)
