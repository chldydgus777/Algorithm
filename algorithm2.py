# 그룹단어 체커 [https://www.acmicpc.net/problem/1316]
#----------------------------------------1316----------다시풀어보기
# n = int(input())

# num = 0
# for _ in range(n):n = int(input())

# num = 0
# for _ in range(n):
#     word = input()
#     for i in range(len(word)):
#         if i != len(word)-1 :
#             if word[i] == word[i+1]:
#                 pass
#             elif word[i] in word[i+1:]:
#                 break
#         else :
#             num += 1 


# 설탕 배달 [https://www.acmicpc.net/problem/2839]
#----------------------------------------2839----------
# sugar = int(input())
# bag = 0

# while True:
#     if sugar % 5 == 0:
#         bag = bag + (sugar // 5)
#         print(bag)
#         break
    
#     sugar -= 3
#     bag += 1 
    
#     if sugar < 0 :
#         print(-1)
#         break



#Fly me to the Alpha Centauri [https://www.acmicpc.net/problem/1011]
#----------------------------------------1011----------



# 베르트랑 공준 [https://www.acmicpc.net/problem/4948]
#----------------------------------------4948----------
# from sys import stdin
# import math
# read = stdin.readline

# def sosu(i):
#   if i%2 ==0 and i != 2:
#     return False
#   for j in range(2, int(math.sqrt(i))+1):
#     if i%j ==0:
#       return False
#   return True
  
# lst = []
# for k in range(2, 2*(123456)+1):
#   if sosu(k):
#     lst.append(k)

# while True:
#   N  = int(read())
#   if N == 0:
#     break

#   cnt = 0
#   for x in lst:
#     if N < x <= N*2:
#       cnt += 1

#   print(cnt)


# 영화감독 숌 [https://www.acmicpc.net/problem/1436]
#----------------------------------------1436----------
# N = int(input())
# movie = 666
# # N = 2 
# while N:
#     if "666" in str(movie): 
#         N -= 1  
#     movie += 1  
#     print(movie - 1)



