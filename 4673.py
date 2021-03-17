# 셀프넘버 [https://www.acmicpc.net/problem/4673]
#----------------------------------------4673----------
def d(n):
    value = n
    for c in str(n):
        value += int(c)
    return value

list = []
for l in range(1,10001):
    list.append(d(l))

for i in range(1,10001):
    if i not in list :
        print(i)