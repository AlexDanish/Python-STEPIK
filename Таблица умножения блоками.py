print('Таблица умножения блоками')
print('Введите числа сначала первого, потом второго отрезка')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, d+1):
    print('\t', j, end='')
print()
for i in range(a, b+1):         
    print(i, '\t', end='')
    for j in range(c, d+1):        
        print(i * j, '\t', end='')
    print()
