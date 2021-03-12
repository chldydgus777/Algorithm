# 구구단
#----------------------------------------2739----------
# n = int(input())


# for i in range(1, 10) :
#     print( '{0} * {1} = {2}'.format(n , i , n * i))


# A + B -3
#----------------------------------------10950----------
# t_c = int(input())

# for i in range(t_c):
#     a, b = map(int, input().split())
#     print(a + b)


# 합
#----------------------------------------8393----------
# n = int(input())
# sum = 0
# for i in range(n+1):
#     sum += i 
# print(sum)


# 빠른 A+B
#----------------------------------------15552----------
# import sys
# t = sys.stdin.readline()
# t = int(t)

# for _ in range(t):
#     j, k = map(int, sys.stdin.readline().split())
    
#     print(j + k)


# N찍기
#----------------------------------------2741----------
# n = input()
# n = int(n)

# for i in range(n):
#     print(i+1)


# 기찍N
#----------------------------------------2742----------
# n = input()
# n = int(n)

# for i in range(n):
#     print(n-i)


# A+B - 7
#----------------------------------------11021----------
# import sys
# t = sys.stdin.readline()
# t = int(t)
#
# for i in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     print(f'Case #{i+1}:', a + b)


# A+B - 8
#----------------------------------------11022----------
# import sys
# t = sys.stdin.readline()
# t = int(t)
#
# for i in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     print(f'Case #{i+1}:', f"{a} + {b} =",a + b)



# 별 찍기 - 1
#----------------------------------------2438----------
# import sys
#
# a = sys.stdin.readline()
# a = int(a)
# for i in range(1, a+1):
#     print('*' * i)


# 별 찍기 - 2
#----------------------------------------2439----------
# a = int(input())
# for i in range(a):
#     i += 1
#     print(" " * (a-i) + "*" * i)


# X보다 작은 수
#----------------------------------------10871----------
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
#
# for i in range(n):
#     if a[i] < x :
#         print(a[i], end=" ")


n = int(input())

for i in range (n):
    a = input().split()
    print(i)








