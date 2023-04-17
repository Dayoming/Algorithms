T = int(input())

for _ in range(T):
    n = int(input())
    dp = [1, 1, 1]
    answer = 0

    for i in range(3, n):
        answer = dp[i - 3] + dp[i - 2]
        dp.append(answer)
    
    print(dp[-1])