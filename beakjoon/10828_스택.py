import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    
    # 정수 x를 스택에 넣는 연산
    if command[0] == 'push':
        stack.append(command[1])
    # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        # 스택에 들어있는 정수가 없는 경우 -1 출력
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    