# 자료 구조, 큐
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
arr = deque([i for i in range(1, n + 1)])
answer = []

pointer = k

# 큐가 존재하는 동안
while arr:
    # 음수면 왼쪽, 양수면 오른쪽으로 회전
    # 큐를 회전하며 맨 왼쪽에 있는 수 제거
    arr.rotate(-(k - 1))
    answer.append(arr.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))