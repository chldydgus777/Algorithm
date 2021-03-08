# 111
# a,b = input().split()
# a = int(a)
# b = int(b)

# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)



# 222
# a = int(input())
# b = int(input())

# print(a*(b%10))
# print(a*((b%100)//10))
# print(a*(b//100))
# print(a*b)



# 333
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




# 444
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

# 555

# for x in range(int(input())):
#    i = list(map(int, input().split()))
#    j = sum(i[1:]) / i[0]
#    count = 0
#    for k in i[1:]:
#        if j > average :
#            count += 1 
#            print (j)


# # # 각 케이스마다 한 줄씩 평균을 넘는 
# # # 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

# n = int(input()) 

# for i in range(0,n): 
#     # range는 0번부터 n번까지 돌린다 n값이 들어오면 0-n까지 for가 돔
#     l = list(input().split())
#     sum = 0
#     studentNum = int(l[0])
    
#     for j in range(1,len(l)): 
# #len은 length, range를 1부터 돌리는 이유는 성적이 1번부터 담겨있기때문에
#         sum +=int(l[j])
#         # 각 점수의 합계를 구한다
#     avg = sum/studentNum #평균을 구함
#     cnt = 0
#     for k in range(1,len(l)): 
#         if int(l[k]) > avg :
#             cnt += 1

#     percent = cnt / studentNum * 100 
#     # 퍼센트로 만들어주기위해 100을 곱해줌
#     print("%.3f" % percent + "%")
#     # %.3f % 퍼센트의 소수점을 제한하는 치트시트

for i in range(int(input())):
    j = list(map(int, input().split()))
    average = sum(j[1:]) / j[0]
    cnt = 0 
    for l in range(1, len(j)):
        if j[l] > average : 
            cnt += 1 
    st_aver = (cnt / j[0] * 100)
    print(format(st_aver, ".3f")+"%")
