# 스택
import sys

n = int(input())
stack = []

for i in range(n):
    # input().split()을 사용할 경우 시간초과
    # Python에서 입력을 받는 가장 빠른 방법이므로 앞으로 이렇게 사용하기!
    command = sys.stdin.readline().split()
    # 정수 X를 스택에 넣는다
    if command[0] == 'push':
        stack.append(command[1])
    # 스택의 가장 위에 있는 정수 출력. 스택에 들어있는 정수가 없는 경우 -1을 출력
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    # 스택에 들어있는 정수의 개수 출력
    elif command[0] == 'size':
        print(len(stack))
    # 스택이 비어있으면 1, 아니면 0을 출력
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력.
    # 만약 스택에 들어있는 정수가 없는 경우 -1을 출력
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            num = stack.pop(-1)
            print(num)
