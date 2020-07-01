'''
Даны три целых числа.
Найдите наибольшее из них (программа должна вывести ровно одно целое число).
'''
A = int(input())
B = int(input())
C = int(input())
if A >= B and A >= C:
    print(A)
elif B >= A and B >= C:
    print(B)
else:
    print(C)
