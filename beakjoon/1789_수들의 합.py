s = int(input())
n = 1

while n * (n + 1) / 2 <= s: # 등차수열의 합이 s보다 작거나 같은 동안
    n = n + 1
print(n - 1) # s보다 커지면 1을 뺀다.