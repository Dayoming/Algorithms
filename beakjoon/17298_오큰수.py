import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
answer = [-1 for _ in range(n)]
stack = [0]

for i in range(1, n):
    # 만약 스택이 비어있지 않고 numbers[i]가 numbers[스택의 가장 위쪽에 존재하는 index] 보다 크다면
    while stack and numbers[i] > numbers[stack[-1]]:
        # 해당 인덱스의 오큰수를 numbers[i]로 저장
        answer[stack[-1]] = numbers[i]
        # 스택의 가장 위 요소를 지워준다.
        stack.pop()
    stack.append(i)

print(*answer)