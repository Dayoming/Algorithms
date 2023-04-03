import sys

n = int(sys.stdin.readline())
answer = 0

for _ in range(n):
    stack = []
    word = sys.stdin.readline().rstrip()

    for i in word:
        # 만약 스택이 비어있지 않고, 마지막 값과 현재 값이 A면 삭제
        if stack and stack[-1] == 'A' and i == 'A':
            stack.pop()
        # 만약 스택이 비어있지 않고, 마지막 값과 현재 값이 B면 삭제
        elif stack and stack[-1] == 'B' and i == 'B':
            stack.pop()
        # 스택이 비어있으면 i를 스택에 추가
        else:
            stack.append(i)
    
    if len(stack) == 0:
        answer += 1

print(answer)