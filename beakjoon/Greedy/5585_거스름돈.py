import sys

n = 1000 - int(sys.stdin.readline())
coins = [500, 100, 50, 10, 5, 1]
idx = 0
answer = 0

while idx < len(coins):
    if n - coins[idx] >= 0:
        n = n - coins[idx]
        answer += 1
    else:
        idx += 1

print(answer)