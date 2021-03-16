# 사칙연산
#----------------------------------------10869----------
# a,b = input().split()
# a = int(a)
# b = int(b)

# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)


# 곱셈
#----------------------------------------2588----------
# a = int(input())
# b = int(input())

# print(a*(b%10))
# print(a*((b%100)//10))
# print(a*(b//100))
# print(a*b)


# 알람시계
#----------------------------------------2884----------
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
#----------------------------------------1110----------
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
#----------------------------------------4344----------
# for i in range(int(input())):
#     j = list(map(int, input().split()))
#     average = sum(j[1:]) / j[0]
#     cnt = 0 
#     for l in range(1, len(j)):
#         if j[l] > average : 
#             cnt += 1  
#     st_aver = (cnt / j[0] * 100)
#     print(format(st_aver, ".3f")+"%")


# C = int(input())

# for i in range(C):
#     j = list(map(int, input().split()))
#     average = sum(j[1:]) / j[0]
#     count = 0
#     for l in range(1, len(j)):
#         if j[l] > average :
#             count += 1
#     student_average = (count / j[0] * 100)
#     print(format(student_average, ".3f")+"%")





# 셀프넘버
#----------------------------------------4673----------
# def d(n):
#     value = n
#     for c in str(n):
#         value += int(c)
#     return value

# list = []
# for l in range(1,10001):
#     list.append(d(l))

# for i in range(1,10001):
#     if i not in list :
#         print(i)


#단어공부
#----------------------------------------1157----------
# a = input().upper()

# bet = list(set(a))
# count = 0
# b = []
# for char in bet:
#     cnt = a.count(char)
#     if cnt >= count :
#         if cnt == count :
#             b.append(char)
#         else :
#             b = []
#             b.append(char)
#         count =  cnt
# if len(b) >= 2 :
#     print('?')
# else :
#     print(b[0])


#크로아티아 알파벳
#----------------------------------------2941----------
# alphabet = str(input())

# Croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in Croatia_list: 
#     alphabet = alphabet.replace(i,'*')

# print(len(alphabet))


#달팽이는 올라가고싶다
#----------------------------------------2869----------
# up, down, top = map(int, (input().split()))

# day = (top - down) / (up - down)

# if int(day) == day:
#     print(int(day))
# else:
#     print(int(day) + 1)


#ACM 호텔
#----------------------------------------10250----------
# a = int(input())

#     for i in range(a):
#         h, w, n = map(int, input().split())
#         if h % n == 0:
#             room = (n // h)
#             floor = h * 100
#         else :
#             room = (n // h) + 1
#             floor = (n % h) * 100
#         print(floor + room)


#소수 구하기
#----------------------------------------1929----------
# def prime(num):
#     if num < 2:
#         return False 

#     i = 2 
#     while i * i <= num :
#         if num % i == 0:
#             return False
#         i += 1
#     return True

# m, n = map(int, input().split())

# for i in range(m, n+1 ):
#     if prime(i):
#         print(i)



# 더하기 사이클

N = int(input())
n = N
other = -1
cycle = 0

while other != N :
    v1 = (n//10) + (n%10)
    v2 = (v1%10) + ((n%10)*10)
    other = v2
    n = v2
    cycle += 1
    
print(cycle)


