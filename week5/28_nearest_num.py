# Напишите программу, которая находит в массиве элемент,
# самый близкий по величине к данному числу.

n = int(input())
myl = list(map(int, input().split()))
x = int(input())
b = []
for i in myl:
    if i > x:
        b.append(i - x)
    else:
        b.append(x - i)
m = ''
ind = ''
for k in range(len(b)):
    if m == '':
        m = b[k]
        ind = k
    else:
        if b[k] < m:
            m = b[k]
            ind = k
print(myl[ind])
