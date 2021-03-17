#단어공부 [https://www.acmicpc.net/problem/1157]
#----------------------------------------1157----------
a = input().upper()

bet = list(set(a))
count = 0
b = []
for char in bet:
    cnt = a.count(char)
    if cnt >= count :
        if cnt == count :
            b.append(char)
        else :
            b = []
            b.append(char)
        count =  cnt
if len(b) >= 2 :
    print('?')
else :
    print(b[0])