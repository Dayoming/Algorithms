# 문자열
import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    print(s[0], s[-1], sep='')