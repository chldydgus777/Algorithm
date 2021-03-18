#deque 회전하는 큐 풀어보기 
from collections import deque

# 덱 자료형으로 리스트 초기화
a_list = deque()

# ‘item’을 덱의 맨 뒤에 넣는다
a_list.append(‘item’)

# ‘item’을 덱의 맨 앞에 넣는다
a_list.appendleft(‘item’)

# 덱의 맨 앞 요소를 뺀다
a_list.popleft() = pop(0)

# 덱의 맨 뒤 요소를 뺀다
a_list.pop()

# 덱의 맨 뒤 요소를 맨 앞으로 보낸다. (양수의 개수만큼)
a_list.rotate(양수)

# 덱의 맨 앞 요소를 맨 뒤로 보낸다 (음수의 개수만큼)
a_list.rotate(음수)

#숫자를 많이 대입해서 풀어보기