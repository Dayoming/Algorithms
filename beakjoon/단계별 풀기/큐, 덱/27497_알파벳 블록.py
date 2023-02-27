import sys
from collections import deque

N = int(sys.stdin.readline())
command = []
temp = deque()
answer = deque()

for _ in range(N):
    command.append(sys.stdin.readline().rstrip())

for i in command:
    i = i.split()
    if i[0] == '1':
        answer.append(i[1])
        temp.append(1)
    elif i[0] == '2':
        answer.appendleft(i[1])
        temp.append(2)
    else:
        if temp:
            if temp.pop() == 1:
                answer.pop()
            else:
                answer.popleft()

if len(answer) != 0:
    print(''.join(answer))
else:
    print(0)
