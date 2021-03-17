#달팽이는 올라가고싶다 [https://www.acmicpc.net/problem/2869]
#----------------------------------------2869----------
up, down, top = map(int, (input().split()))

day = (top - down) / (up - down)

if int(day) == day:
    print(int(day))
else:
    print(int(day) + 1)