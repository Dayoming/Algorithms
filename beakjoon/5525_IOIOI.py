import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
cnt = 0

P = 'I' + ('OI' * n)

for i in range(m - (n + 2) + 1):
    if s[i:i + len(P)] == P:
        cnt += 1

print(cnt)        