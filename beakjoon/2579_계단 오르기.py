n = int(input())
dp = [0 for _ in range(301)]
stair = []

for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[0])
    exit(0)
elif n == 2:
    print(stair[0] + stair[1])
    exit(0)

# 한 칸을 간 경우 저장
dp[0] = stair[0]
# 한 칸씩 두 칸을 간 경우, 혹은 한번에 두 칸을 간 경우 중 큰 값 저장
dp[1] = max(stair[0] + stair[1], stair[1])
# 한칸 + 두칸, 두칸 + 한칸인 경우 중 큰 값 저장
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2], dp[i - 3] + stair[i - 1]) + stair[i]
    
print(dp[n - 1])