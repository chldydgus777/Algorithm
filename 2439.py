# 별 찍기 -2 [https://www.acmicpc.net/problem/2439]
#----------------------------------------2439----------
import sys 
N = int(sys.stdin.readline())

for i in range(1, N+1) :
    for j in range(i) :
        print(i)