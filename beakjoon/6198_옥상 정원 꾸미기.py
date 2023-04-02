import sys

n = int(sys.stdin.readline())
buildings = []
answer = 0

for _ in range(n):
    buildings.append(int(sys.stdin.readline()))

stack = []
for i in range(n):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()
        
    stack.append(buildings[i])
    answer += len(stack) - 1

print(answer)