# 더하기사이클 [https://www.acmicpc.net/problem/1110]
#----------------------------------------1110----------
start = int(input())
instead = start
other = 101
num = 0

while other != start :
    value = (instead // 10)+(instead % 10)
    value1 = (value % 10)+((instead % 10)* 10)
    other = value1
    instead = value1
    num = num + 1 

print(num)