# Выведите все элементы списка с четными индексами
# (то есть A[0], A[2], A[4], ...).
# Программа должна быть эффективной и не выполнять лишних действий!

A = list(map(str, input().split()))
for i in range(len(A)):
    if i % 2 == 0:
        print(A[i], end=' ')