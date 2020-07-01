# По данному натуральном n вычислите сумму 1²+2²+3²+...+n².

n = int(input())
s = 0
for i in range(n):
    s += (i + 1)**2
print(s)
