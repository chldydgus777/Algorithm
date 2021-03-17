# 평균은 넘겠지 [https://www.acmicpc.net/problem/4344]
#----------------------------------------4344----------
for i in range(int(input())):
    j = list(map(int, input().split()))
    average = sum(j[1:]) / j[0]
    cnt = 0 
    for l in range(1, len(j)):
        if j[l] > average : 
            cnt += 1  
    st_aver = (cnt / j[0] * 100)
    print(format(st_aver, ".3f")+"%")
