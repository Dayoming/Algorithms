# 다이나믹 프로그래밍
import sys

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n - 3) + solution(n - 2) + solution(n - 1)

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    print(solution(n))