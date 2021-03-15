input = [3, 5, 6, 1, 2, 4]

# 지정변수
def find_max_num(array):
    max_num = array[0] # 초기값 설정
    for num in array:
        if num > max_num: # 초기값보다 num이 크면 
            max_num = num #  max_num에 num 대입

    return max_num # 반복문이 끝나면 max_num에는 제일 큰 변수가 들어있다

result = find_max_num(input)
print(result)
