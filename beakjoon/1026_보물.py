# 그리디 알고리즘
# 보물
import sys

n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# B의 가장 큰 수는 A의 가장 작은 수와 매칭
# B의 가장 작은 수는 A의 가장 큰 수와 매칭
s = 0
for i in range(n):
    # 두 수를 곱해주고 s에 더한다
    s += max(A) * min(B)
    # 각각 A와 B에서 해당하는 수를 지워줌
    A.pop(A.index(max(A)))
    B.pop(B.index(min(B)))

print(s)