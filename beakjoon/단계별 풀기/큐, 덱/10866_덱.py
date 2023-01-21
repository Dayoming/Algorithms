import sys
from collections import deque

n = int(sys.stdin.readline())
save = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        save.appendleft(command[1])
    elif command[0] == 'push_back':
        save.append(command[1])
    elif command[0] == 'pop_front':
        if len(save) == 0:
            print(-1)
        else:
            print(save.popleft())
    elif command[0] == 'pop_back':
        if len(save) == 0:
            print(-1)
        else:
            print(save.pop())
    elif command[0] == 'size':
        print(len(save))
    elif command[0] == 'empty':
        if len(save) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(save) == 0:
            print(-1)
        else:
            print(save[0])
    elif command[0] == 'back':
        if len(save) == 0:
            print(-1)
        else:
            print(save[-1])