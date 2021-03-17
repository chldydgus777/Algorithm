# 알람시계 [https://www.acmicpc.net/problem/2884]
#----------------------------------------2884----------
H,M = input().split()
H = int(H)
M = int(M)

if (M < 45):
    wake_up_minute = M + 15
    if (H != 0):
        wake_up_hour = H - 1
    else :
        wake_up_hour = 23
else:
    wake_up_minute = M - 45
    wake_up_hour = H
    
print(wake_up_hour, wake_up_minute)