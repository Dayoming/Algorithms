import sys

# 사람의 수
n = int(sys.stdin.readline())
# 각 사람이 돈을 인출하는데 걸리는 시간
P = list(map(int, sys.stdin.readline().split()))
temp = 0
answer = []

P.sort()

for i in P:
    temp += i
    answer.append(temp)

print(sum(answer))