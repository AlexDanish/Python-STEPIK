print('Cуммa чисел до первого 0')
# Напишите программу, которая считывает
# со стандартного ввода целые числа, 
# по одному числу в строке, и 
# после первого введенного нуля выводит
# сумму полученных на вход чисел.
print('Вводите числа')
a = int(input())
i = a
s = 0
while i != 0:
    s += i
    i = int(input())
print(s)