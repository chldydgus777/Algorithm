# ACM 호텔 [https://www.acmicpc.net/problem/10250]
#----------------------------------------10250----------
a = int(input())

    for i in range(a):
        h, w, n = map(int, input().split())
        if h % n == 0:
            room = (n // h)
            floor = h * 100
        else :
            room = (n // h) + 1
            floor = (n % h) * 100
        print(floor + room)
