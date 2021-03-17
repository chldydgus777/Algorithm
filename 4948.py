# 베르트랑 공준 [https://www.acmicpc.net/problem/4948]
#----------------------------------------4948----------
from sys import stdin
import math
read = stdin.readline

def sosu(i):
  if i%2 ==0 and i != 2:
    return False
  for j in range(2, int(math.sqrt(i))+1):
    if i%j ==0:
      return False
  return True

lst = []
for k in range(2, 2*(123456)+1):
  if sosu(k):
    lst.append(k)

while True:
  N  = int(read())
  if N == 0:
    break

  cnt = 0
  for x in lst:
    if N < x <= N*2:
      cnt += 1

  print(cnt)
