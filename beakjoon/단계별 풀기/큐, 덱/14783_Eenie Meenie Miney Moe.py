# 구현, 자료 구조, 시뮬레이션, 큐
import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
# 이동할 수들을 큐로 정의
counts = deque(list(map(int, sys.stdin.readline().split())))
arr = deque([i for i in range(1, n + 1)])

while len(arr) != 1:
    # 현재 몇 칸 이동해야하는지 꺼낸다
    count = counts.popleft()
    # 큐를 돌려서 이동하고 제거
    arr.rotate(-(count - 1))
    arr.popleft()
    # 꺼낸 수를 다시 맨 뒤로 넣는다
    counts.append(count)

print(arr[0])
