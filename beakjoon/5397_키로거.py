import sys

n = int(sys.stdin.readline())

for _ in range(n):
    command = list(sys.stdin.readline().rstrip())

    stack1 = []
    stack2 = []
    
    for i in command:
        # 커서를 왼쪽으로 1만큼 움직인다
        if i == '<':
            if stack1:
                stack2.append(stack1.pop())
        # 커서를 오른쪽으로 1만큼 움직인다
        elif i == '>':
            if stack2:
                stack1.append(stack2.pop())
        # 커서의 왼쪽에 글자가 존재하면 그 글자를 지운다
        elif i == '-':
            if stack1:
                stack1.pop()
        # 그 외의 문자열이라면 첫 번째 스택에 추가해준다
        else:
            stack1.append(i)
        
    print(''.join(stack1 + stack2[::-1]))