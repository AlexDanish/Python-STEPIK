print('Площадь комнаты')
print('Введите тип комнаты и её стороны')
print('треугольник,a,b,c')
print('прямоугольник,a,b')
print('круг, r')
F = input()
if F=='треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p-c)) ** 0.5)
if F=='прямоугольник':
    a = int(input())
    b = int(input())
    print(a*b)
if F=='круг':
    Pi=3.14
    r = int(input())
    print(Pi*r**2)
