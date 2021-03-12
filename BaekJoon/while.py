# A+B -5
#----------------------------------------10952----------
# while(True):
#     a, b = list(map(int, input().split()))
#     if(a == 0 and b == 0):
#         break
#     else :
#         print(a+b)

# A+B -4
#----------------------------------------10951----------
# while(True):
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break


# 더하기 사이클
#---------------------------------------10951----------
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
