# A+B - 7 [https://www.acmicpc.net/problem/11021]
#----------------------------------------11021----------
import sys

C = int(sys.stdin.readline())

for i in range(C):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}:", A+B)
