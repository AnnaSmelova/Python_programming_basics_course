'''
Переставьте цифры числа в обратном порядке
'''
N = int(input())
k = ''
while N // 10 != 0:
    k += str(N % 10)
    N = N // 10
k = k + str(N)
print(k)
