# 그룹단어 체커
#----------------------------------------1316----------
n = int(input())

num = 0
for _ in range(n):n = int(input())

num = 0
for _ in range(n):
    word = input()
    for i in range(len(word)):
        if i != len(word)-1 :
            if word[i] == word[i+1]:
                pass
            elif word[i] in word[i+1:]:
                break
        else :
            num += 1 
            