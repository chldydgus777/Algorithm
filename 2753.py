# 윤년 [https://www.acmicpc.net/problem/2753]
#----------------------------------------2753----------
A = int(input())

if A % 4 == 0 and A % 100 != 0 or A % 400 == 0 :
    print("1")
else : 
    print("0")