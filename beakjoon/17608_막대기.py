import sys

n = int(sys.stdin.readline())
sticks = []
answer = 0

for _ in range(n):
    sticks.append(int(sys.stdin.readline()))

temp = sticks[-1]

# 오른쪽에서부터 
for i in range(n - 1, -1, -1):
    if temp < sticks[i]:
        answer += 1
        temp = sticks[i]

print(answer + 1)