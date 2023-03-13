# 1이 될 때까지
N, K = map(int, input().split())
answer = 0

while N != 1:
    if N % K == 0:
        N = N // K
        answer += 1
    else:
        N = N - 1
        answer += 1

print(answer)