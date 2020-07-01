'''
Дан многочлен P(x) = a[n] xⁿ+a[n-1] xⁿ⁻¹+...+a[1] x+a[0] и число x.
Вычислите значение этого многочлена, воспользовавшись схемой Горнера:

P(x) = ( ... ( ( ( a[n] x + a[n-1] ) x + a[n-2] ) x + a[n-3] ) ... ) x + a[0]
'''
n = int(input())
x = float(input())
a = float(input())
r = a * x
if n != 0 and n != 1:
    for i in range(n - 1):
        a = float(input())
        r = (r + a) * x
    a = float(input())
    r = r + a
elif n == 0:
    r = a
else:
    a = float(input())
    r = r + a
print(r)
