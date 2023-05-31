import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    command = sys.stdin.readline().split()
    
    # 정수 x를 큐에 넣는 연산
    if command[0] == 'push':
        queue.append(command[1])
    # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
    elif command[0] == 'pop':
        if queue:
            print(queue.pop(0))
        # 큐에 들어있는 정수가 없는 경우 -1 출력
        else:
            print(-1)
    # 큐에 들어있는 정수의 개수 출력
    elif command[0] == 'size':
        print(len(queue))
    # 큐가 비어있으면 1, 아니면 0 출력
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    # 큐의 가장 앞에 있는 정수를 출력, 큐에 들어있는 정수가 없으면 -1 출력
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    # 큐의 가장 뒤에 있는 정수를 출력, 큐에 들어있는 정수가 없으면 -1 출력
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)