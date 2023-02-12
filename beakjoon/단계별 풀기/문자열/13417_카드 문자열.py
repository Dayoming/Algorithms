# 자료 구조, 문자열, 그리디 알고리즘, 덱
import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(sys.stdin.readline().rstrip().split())

    answer = deque([arr[0]])

    for i in range(1, len(arr)):
        if arr[i] <= answer[0]:
            answer.appendleft(arr[i])
        else:
            answer.append(arr[i])
    
    print(''.join(answer))
