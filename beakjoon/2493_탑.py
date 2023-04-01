import sys

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
answer = [0 for i in range(n)]
stack = [n - 1]

for i in range(n - 2, -1, -1):
    while stack and tower[i] > tower[stack[-1]]:
        answer[stack[-1]] = i + 1
        stack.pop()
    stack.append(i)

print(*answer)

