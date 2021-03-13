input = 20

#소수는 본인과 1외 에는 아무것도 나눌 수 없다.
#주어진 자연수 N이 소수이기 위한 필요 충분 조건은 
#N이 N의 제곱근보다 크지않은 어떤 소수로도 나눠지지 않는다.

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1): # n의 범위 2 ~ number + 1 
        for i in prime_list: #i의 범위 2 ~ number - 1  
            if n % i == 0 and i * i <= n :
                break
        else :
            prime_list.append(n)


    return prime_list


result = find_prime_list_under_number(input)
print(result)