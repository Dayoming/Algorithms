n = int(input())

build = []
rank = []

for _ in range(n):
    height, weight = map(int, input().split())
    build.append([height, weight])

for i in range(n):
    k = 0
    for j in range(n):
        # 몸무게와 키가 모두 크면
        if build[i][0] < build[j][0] and build[i][1] < build[j][1]:
            k += 1
    rank.append(k + 1)

print(*rank)