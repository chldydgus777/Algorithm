# 사분면 구하기 [https://www.acmicpc.net/problem/14681]
#----------------------------------------14681----------
X = int(input())
Y = int(input())


if X > 0 and Y > 0 :
    print("1")
elif X < 0 and Y > 0 :
    print("2")
elif X < 0 and Y < 0 :
    print("3")
elif X > 0 and Y < 0 :
    print("4")
