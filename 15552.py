# 빠른 A + B [https://www.acmicpc.net/problem/15552]
#----------------------------------------15552----------
import sys

C = int(sys.stdin.readline())
for i in range(C):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)