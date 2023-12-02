print('Геномные последовательности GC в %')
print('Введите геномную последовательность')
s = input()

a = len(s)
n = s.upper().count('g'.upper())
m = s.upper().count('c'.upper())
    
print((n + m) / a * 100)