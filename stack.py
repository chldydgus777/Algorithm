#stack 사용 제로 풀어보기
#python에서는 list형을 사용
a_list = [‘스파르타’]

#스택에서 맨 뒤에 요소 추가, 즉 push 연산은 append
a_list.append(“용현”)
-> a_list = [‘스파르타’,‘용현']

#스택에서 맨 뒤에 요소 삭제, 즉 pop은 pop
a_list.pop()
-> 용현 삭제, a_list = [‘스파르타']

#스택에서 맨 앞에 요소 삭제, pop(0) 쓰면 안되긴함
a_list.pop(0)
->스파르타 삭제, a_list = []

#stack

#push

#pop

#peek
#a = a_list[-1]
#a = ‘용현’
a.sort(reverse=True)내림차순
a.sort() 오름차순

