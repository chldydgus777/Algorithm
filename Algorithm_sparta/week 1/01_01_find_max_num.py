input = [3, 5, 6, 1, 2, 4]

# find_max_num을 다른숫자들과 비교하는 방식 
# 이중반복문
def find_max_num(array):
    for num in array : # 배열의 숫자를 하나하나 꺼내서 나열
        for num2 in array : # 비교할 변수를 나열
            if num < num2 :
                break
        else : # for문이 다 돌때까지 한번도 break 하지 않는다면 
            return num # 최종값 return


result = find_max_num(input)
print(result)