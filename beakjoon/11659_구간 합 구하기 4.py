import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
# 누적 합 배열 이용
prefix_sum = [0 for _ in range(n + 1)]

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + numbers[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i - 1])