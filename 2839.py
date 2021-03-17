# 설탕 배달 [https://www.acmicpc.net/problem/2839]
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