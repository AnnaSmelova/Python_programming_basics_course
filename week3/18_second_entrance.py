'''
Дана строка. Найдите в этой строке второе вхождение буквы f и выведите индекс этого вхождения.
Если буква f в данной строке встречается только один раз,
выведите число -1, а если не встречается ни разу, выведите число -2.
При решении этой задачи нельзя использовать метод count.
'''
s = input()
pos = s.find('f')
if pos == -1:
    print(-2)
else:
    pos = s.find('f', pos + 1)
    if pos == -1:
        print(-1)
    else:
        print(pos)