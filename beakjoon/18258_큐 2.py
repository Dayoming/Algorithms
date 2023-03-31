import sys
from collections import deque

n = int(sys.stdin.readline())
# 정수를 저장하는 큐 초기화
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
