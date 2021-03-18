# X보다 작은 수  [https://www.acmicpc.net/problem/10871]
#----------------------------------------10871----------
import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if A[i] < X :
        print(A[i], end=" ")