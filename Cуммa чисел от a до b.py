print('Cуммa чисел от a до b')
print('Введите a и b')
a = int(input())
b = int(input())
s = 0
i = a
while i <= b:
    s += i
    i += 1
print(s)