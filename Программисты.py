print('Программисты')
print('Введите число программистов')

a = ('программист')
b = ('программиста')
c = ('программистов')
d = int(input())

if d%10==1 and not d%100==11:
    print(d, a)
if d%100==11 or d%100==12 or d%100==13 or d%100==14 or d%10==0 or d%10==5 or d%10==6 or d%10==7 or d%10==8 or d%10==9:
    print(d, c)
elif not d%10==1:
    print(d, b)