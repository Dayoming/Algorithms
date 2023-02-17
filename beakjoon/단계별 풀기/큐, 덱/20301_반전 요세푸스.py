# 구현, 자료 구조, 시뮬레이션, 덱
import sys
from collections import deque

n, k, m = map(int, sys.stdin.readline().split())
peoples = deque([i for i in range(1, n + 1)])
way = True
cnt = 0

while peoples:
    if cnt == m:
        way = not way
        cnt = 0
    
    if way == True:
        peoples.rotate(-(k - 1))
        print(peoples.popleft())
        cnt += 1
    else:
        peoples.rotate(k)
        print(peoples.popleft())
        cnt += 1