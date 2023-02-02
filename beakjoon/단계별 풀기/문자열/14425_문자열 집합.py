# 문자열 집합
import sys

n, m = map(int, sys.stdin.readline().split())
s = []
check = []
cnt = 0

for i in range(n):
    s.append(sys.stdin.readline().rstrip())

for j in range(m):
    check.append(sys.stdin.readline().rstrip())

for k in check:
    if k in s:
        cnt += 1

print(cnt)