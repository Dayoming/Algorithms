n = int(input())
dp = [0 for i in range(50001)]
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3

for i in range(5, n + 1):
    dp[i] = dp[i - 4] + dp[i - 3] + dp[i - 2]

print(dp[n] % 1000000009)