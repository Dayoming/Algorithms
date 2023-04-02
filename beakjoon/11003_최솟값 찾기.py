import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
# 최소값을 구할 범위
queue = deque([])

for i in range(n):
    # 범위를 벗어나는 원소(맨 앞의 원소) 삭제
    if queue and queue[0][0] <= i - l:
        queue.popleft()
    
    # 들어올 원소가 기존의 원소보다 작으면 삭제
    while len(queue) >= 1 and A[i] < queue[-1][1]:
        queue.pop()
    
    # 들어올 원소 추가
    queue.append((i, A[i]))

    print(queue[0][1], end = ' ')