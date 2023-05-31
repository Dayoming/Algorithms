import sys

n = int(sys.stdin.readline())
deque = []

for _ in range(n):
    command = sys.stdin.readline().split()
    
    # 정수 x를 덱의 앞에 넣는다
    if command[0] == 'push_front':
        temp = [command[1]]
        deque = temp + deque
    # 정수 x를 덱의 뒤에 넣는다
    elif command[0] == 'push_back':
        deque.append(command[1])
    # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력. 덱에 들어있는 정수가 없으면 -1
    elif command[0] == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력. 만약, 덱에 들어있는 정수가 없으면 -1
    elif command[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    # 덱에 들어있는 정수의 개수 출력
    elif command[0] == 'size':
        print(len(deque))
    # 덱이 비어있으면 1, 아니면 0 출력
    elif command[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    # 덱의 가장 앞에 있는 정수를 출력, 큐에 들어있는 정수가 없으면 -1 출력
    elif command[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    # 덱의 가장 뒤에 있는 정수를 출력, 큐에 들어있는 정수가 없으면 -1 출력
    elif command[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)