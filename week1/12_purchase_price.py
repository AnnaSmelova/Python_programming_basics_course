'''
Пирожок в столовой стоит A рублей и B копеек.
Определите, сколько рублей и копеек нужно заплатить за N пирожков.
'''
A = int(input())
B = int(input())
N = int(input())
price = A * 100 + B
total = N * price
print(total // 100, total % 100)
