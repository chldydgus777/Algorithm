# print("a".isalpha())  
# print("1".isalpha())   
# s = "abcdefg"
# print(s[0].isalpha())  

def find_alphabet_occurrence_array(string):
    alphabet_array = [0] * 26 # 알파벳별 빈도수 저장 (길이가 26인 0으로 초기화 된 배열)
    
    for char in string:
        if not char.isalpha(): # char 가 알파벳 이라면 continue // 띄어쓰기 제거
            continue            
        array_index = ord(char) - ord("a") #알바벳 위치를 index로 먹여줌 // a = 0, b = 1, c = 2
        alphabet_array[array_index] += 1 

    return alphabet_array   


print(find_alphabet_occurrence_array("hello my name is sparta"))