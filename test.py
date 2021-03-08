# 사칙연산
# ----------10869------------------------------
# a,b = input().split()
# a = int(a)
# b = int(b)

# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)


# 곱셈
#------------------------------2588------------------------------
# a = int(input())
# b = int(input())

# print(a*(b%10))
# print(a*((b%100)//10))
# print(a*(b//100))
# print(a*b)


# 알람시계
#------------------------------2884------------------------------
# H,M = input().split()
# H = int(H)
# M = int(M)

# if (M < 45):
#     wake_up_minute = M + 15
#     if (H != 0):
#         wake_up_hour = H - 1
#     else :
#         wake_up_hour = 23
# else:
#     wake_up_minute = M - 45
#     wake_up_hour = H
    
# print(wake_up_hour, wake_up_minute)


# 더하기사이클
#------------------------------1110------------------------------
# start = int(input())
# instead = start
# other = 101
# num = 0

# while other != start :
#     value = (instead // 10)+(instead % 10)
#     value1 = (value % 10)+((instead % 10)* 10)
#     other = value1
#     instead = value1
#     num = num + 1 

# print(num)


# 평균은 넘겠지
#------------------------------4344------------------------------
# for i in range(int(input())):
#     j = list(map(int, input().split()))
#     average = sum(j[1:]) / j[0]
#     cnt = 0 
#     for l in range(1, len(j)):
#         if j[l] > average : 
#             cnt += 1  
#     st_aver = (cnt / j[0] * 100)
#     print(format(st_aver, ".3f")+"%")


# 셀프넘버
#------------------------------4673------------------------------
def d(n):
    value = n 
    for c in list(str(n)) :
        value += int(c)
    return value

DAEHO = []
for l in range(1,10001):
    DAEHO.append(d(l))
for i in range(1,10001):
    if i not in DAEHO :
        print(i)
        
    



#단어공부
#------------------------------1157------------------------------




#크로아티아 알파벳
#------------------------------2941------------------------------




#달팽이는 올라가고싶다
#------------------------------2869------------------------------




#ACM 호텔
#------------------------------10250------------------------------




#소수 구하기
#------------------------------1929------------------------------