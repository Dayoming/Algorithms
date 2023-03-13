# 큰 수의 법칙
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
data = data[0:2]

print(data)

answer = 0
count = 0

for i in range(M):
    if count == K:
        answer += data[1]
        count = 0
    else:
        answer += data[0]
        count += 1

print(answer)