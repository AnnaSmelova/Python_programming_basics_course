# В данном списке из n≤10⁵ целых чисел найдите три числа,
# произведение которых максимально.
# Решение должно иметь сложность O(n), где n - размер списка.
# То есть сортировку использовать нельзя.
# Выведите три искомых числа в любом порядке.

myl = list(map(int, input().split()))
a = []
a1, a2, a3 = False, False, False
b = []
b1, b2, b3 = False, False, False

for el in myl:
    if el >= 0:
        a.append(el)
    else:
        b.append(el)

c = b.copy()
c1, c2, c3 = False, False, False

lnga = len(a)
lngb = len(b)
lngc = lngb

if lnga >= 3:
    a1 = max(a)
    a.remove(a1)
    a2 = max(a)
    a.remove(a2)
    a3 = max(a)
    a1, a2, a3 = str(a1), str(a2), str(a3)
elif lnga >= 2:
    a1 = max(a)
    a.remove(a1)
    a2 = max(a)
    a1, a2, = str(a1), str(a2)
elif lnga >= 1:
    a1 = max(a)
    a1 = str(a1)

if lngb >= 3:
    b1 = min(b)
    b.remove(b1)
    b2 = min(b)
    b.remove(b2)
    b3 = min(b)
    b1, b2, b3 = str(b1), str(b2), str(b3)
elif lngb >= 2:
    b1 = min(b)
    b.remove(b1)
    b2 = min(b)
    b1, b2 = str(b1), str(b2)
elif lngb >= 1:
    b1 = min(b)
    b1 = str(b1)

if lngc >= 3:
    c1 = max(b)
    c.remove(c1)
    c2 = max(c)
    c.remove(c2)
    c3 = max(c)
    c1, c2, c3 = str(c1), str(c2), str(c3)
elif lngc >= 2:
    c1 = max(c)
    c.remove(c1)
    c2 = max(c)
    c1, c2 = str(c1), str(c2)
elif lngc >= 1:
    c1 = max(c)
    c1 = str(c1)

ma = -1000000000000000
mb = -1000000000000000
maab = -1000000000000000
mabb = -1000000000000000

if a1 and a2 and a3:
    ma = int(a1) * int(a2) * int(a3)
if a1 and a2:
    if c1:
        maab = int(a1) * int(a2) * int(c1)
if a1:
    if b1 and b2:
        mabb = int(a1) * int(b1) * int(b2)
if c1 and c2 and c3:
    mb = int(c1) * int(c2) * int(c3)

tar = max(ma, mb, maab, mabb)
if tar == ma:
    print(a1, a2, a3)
elif tar == mb:
    print(c3, c2, c1)
elif tar == maab:
    print(c1, a1, a2)
elif tar == mabb:
    print(b2, b1, a1)
