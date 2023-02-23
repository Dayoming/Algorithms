# 다이나믹 프로그래밍
import sys

n = int(sys.stdin.readline())
dp = [1] * 10

for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j - 1]

print(sum(dp) % 10007)
