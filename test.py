# station = '사당','신도림','인천공항'

# print(station , "행 열차가 들어오고 있습니다")

# print(1+1)
# print(3-1)

# print(2**3)


# url = "http://google.com"

# my_url = url.replace("http://", "")
# # print(my_url)
# my_url = my_url[:5]
# print(my_url)
# password  = my_url[:3] + str(len(my_url)) + str(my_url.count("e")) + "!"
# print("{0} 의 비밀번호는 {1}입니다".format(url, password))


# subway = ["김채연", "최용현"]
# print(subway)

# print(subway.index("김채연"))

# subway.append("꼬고")
# print(subway)

# subway.insert(0, "홍대입구")
# print(subway)

# print(subway.pop())
# print(subway)

# subway.append("김채연")
# print(subway)

# print(subway.count("김채연"))

# num_list =[5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)


# num_list.reverse()
# print(num_list)

# cbn = {3: "최용현", 4 : "김채연", 100: "가나다" }

# print(cbn.get(5,  "사용가능")) 

# print(3 in cbn)
# print(5 in cbn)
# cbn["A-3"] = "바보"
# print(cbn)


# del cbn["A-3"]
# print(cbn)
# print(cbn.keys())

# print(cbn.values())

# cbn.clear()
# print(cbn)

# weather = input("오늘 날씨는 어때요? ")

# if weather == '미세먼지':
#     print("마스크를 챙기세요")
# elif weather == '비'or '눈':
#     print("우산을 챙기세요")
# else :
#     print("맑네요 !")


# for waiting_no in range(1, 101):
#     print("대기번호 :{0}".format(waiting_no))

# customer = "용현"
# index = 5
# while index >= 1 :
#     print("{0}님 , 커피가 준비되었습니다 ! 폐기처분까지 {1}번 남았습니다".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("{0}님 , 죄송합니다. 커피는 폐기 되었습니다 ! ".format(customer))


# absent = [2, 5] # 결석 
# no_book = [8]
# for student in range(1, 11):
#     if student in absent :
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지 {0}번 교무실로 따라와".format(no_book))
#         break
#     print("{0}번, 121p 읽어봐".format(student))

# from random import *
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time & time <= 15 :
#         print("[o] {0}번 째 손님 (소요시간 : {1}분".format(i, time))
#         cnt += 1
#     else:
#         print("[] {0}번 째 손님 (소요시간 : {1}분".format(i, time))

# print("총 탑승 고객 : {0}분".format(cnt))

# def open_account():
#     print("계좌가 개설되었습니다. ")

# open_account()

# def profile(name, age, main_lang):
#     print("이름: {0}\t 나이 : {1} 살\t 주사용언어: {2}".format(name, age, main_lang))

# profile("최용현", 25, "리액트")
# profile("가나다", 30, "자바")


# def profile(name, age=17, main_lang='python'):
#     print("이름: {0}\t 나이 : {1} 살\t 주사용언어: {2}".format(name, age, main_lang))
    

# profile("최용현")
# profile("가나다")

def profile(name, age, *lang):
    print("이름 : {0} \t 나이 : {1} 살\t".format(name, age), end=" ")
    for l in lang:
        print(l, end=" ")
    print()

profile("유재석", 20, 'python', 'java', 'C++')
profile("최용현", 30, 'python', "react")
