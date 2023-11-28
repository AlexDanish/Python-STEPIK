print('Нарисуйте_треугольник_2')
print('Введите высоту треугольника n')
n = int(input())
stars = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'