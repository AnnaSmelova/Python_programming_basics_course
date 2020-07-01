# Петя перешёл в другую школу.
# На уроке физкультуры ему понадобилось определить своё место в строю.
# Помогите ему это сделать.

myl = list(map(int, input().split()))
s = int(input())
ind = -1
for i in range(len(myl)):
    if s <= myl[i]:
        ind = i
print(ind + 2)
