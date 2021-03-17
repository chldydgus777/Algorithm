# 별 찍기 -2 [https://www.acmicpc.net/problem/2439]
#----------------------------------------2439----------
N = int(input())

for i in range(N):
    i += 1
    print(" "*(N-i) + "*" *i)