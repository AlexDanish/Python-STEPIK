print('Калькулятор')
print('Введите первое число, операцию и второе число')
A = float(input())
C = input()
B = float(input())
if C=='+':
    print(A+B)
if C=='-':
    print(A-B)
if C=='*':
    print(A*B)
if C=='/':
    print(A/B)
if C=='pow':
    print(A**B)
if C=='div':
    print(A//B)