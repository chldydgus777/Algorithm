input = [4, 5, 6, 1, 2, 3]


def is_number_exist(number, array):
    for element in array :  # array의 길이만큼 아래연산 실행
        if number == element:  # 비교연산
            return True # N * 1 = N 만큼 사용

    return False

result = is_number_exist(3, input)
print(result)