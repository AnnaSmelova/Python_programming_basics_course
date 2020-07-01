# Аня и Боря любят играть в разноцветные кубики,
# причем у каждого из них свой набор и в каждом наборе все
# кубики различны по цвету. Однажды дети заинтересовались,
# сколько существуют цветов таких, что кубики каждого цвета
# присутствуют в обоих наборах. Для этого они занумеровали
# все цвета случайными числами. На этом их энтузиазм иссяк,
# поэтому вам предлагается помочь им в оставшейся части.
# Номер любого цвета — это целое число в пределах от 0 до 10⁹.

in_file = open('input.txt', 'r', encoding='utf8')
# in_file = open('05_cubes.txt', 'r', encoding='utf8')

lines = in_file.readlines()
n, m = list(map(int, lines[0].split()))
a = set()
b = set()
for i in range(1, n + 1):
    string = lines[i].strip()
    a.add(int(string))
for j in range(n + 1, len(lines)):
    string = lines[j].strip()
    b.add(int(string))

inter = list(a & b)
inter.sort()
al = list(a ^ a & b)
al.sort()
bl = list(b ^ a & b)
bl.sort()

print(len(inter))
print(*inter)
print(len(al))
print(*al)
print(len(bl))
print(*bl)
