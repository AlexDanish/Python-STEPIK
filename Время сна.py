print('Високосный ли год')
print('Введите год от 1900 до 3000')
A = int(input())
if A%4==0 and not A%100==0 or A%400==0:
    print('Високосный')
else:
    print('Обычный')
