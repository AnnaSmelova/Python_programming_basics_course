'''
Последовательность Фибоначчи определяется так:

F[0] = 0, F[1] = 1, ..., F[n] = F[n-1] + F[n-2].

По данному числу n определите n-е число Фибоначчи F[n].
'''
n = int(input())
f0 = 0
f1 = 1
fn = 1
i = 2
if n == 0:
    print(f0)
elif n == 1:
    print(f1)
else:
    while i <= n:
        fn = f0 + f1
        f0 = f1
        f1 = fn
        i += 1
    print(fn)
