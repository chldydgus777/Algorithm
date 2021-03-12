# 그룹단어 체커
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


# 설탕 배달
#----------------------------------------2839----------
sugar = int(input())
bag = 0

while True:
    if sugar % 5 == 0:
        bag = bag + (sugar // 5)
        print(bag)
        break
    
    sugar -= 3
    bag += 1 
    
    if sugar < 0 :
        print(-1)
        break
        


# 봉지 종류 2개 3kg, 5kg
# 가능하다면 5kg를 많이들고가는게 benefit
# 최소한의 봉지로 들고가는게 좋다