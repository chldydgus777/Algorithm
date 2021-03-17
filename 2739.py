# 구구단 [https://www.acmicpc.net/problem/2739]
#----------------------------------------2739----------
N = int(input())

for i in range (1, 10):
    print("{0} * {1} = {2}".format(N, i, i * N))