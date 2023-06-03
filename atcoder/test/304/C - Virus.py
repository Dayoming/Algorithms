# 숫자가 매겨진 N명의 사람이 2차원 평면 위에 있다.
# 사람 i는 좌표로 표시되는 점 (X, Y) 위에 있다.
# 사람 1은 바이러스에 감염되었다. 바이러스는 감염된 사람에게서 가까운 사람들에게 퍼지는데,
# 여기서 거리는 유클리드 거리, 즉 두 점에 대해서 정의된다.
# 충분한 시간이 지난 후, 즉 i번째 사람에서 D의 거리에 있는 모든 사람들이
# i번째 사람이 감염되면 i번째 사람이 각각의 i에 대해 바이러스에 감염되었는지 여부를 결정
# 만약 i번째 사람이 바이러스에 감염되었다면 Yes 출력, 아니면 No 출력
from collections import deque

n, d = map(int, input().split())
peoples = deque()
# 감염 여부를 저장할 리스트
infection = ['Yes' for _ in range(n)]
# 감염되지 않은 사람들과 비교할 원본 리스트
temp = list()

for _ in range(n):
    people = list(map(int, input().split()))
    temp.append(people)
    peoples.append(people)

queue = deque()
# 첫 번째 사람은 무조건 감염이므로 큐에 담는다
queue.append(peoples[0])

while queue and peoples:
    x, y = queue.popleft()
    peoples.remove([x, y])
    
    # 나머지 사람들과 거리를 쟀을 때, 가까우면 감염이고 멀먼 감염X
    for i in range(len(peoples)):
        dx, dy = peoples[i]
        if ((x - dx)**2 + (y - dy)**2) ** (1/2) <= d:
            if [dx, dy] not in queue:
                queue.append([dx, dy])

# 감염되지 않은 사람이 존재하면
if peoples:
    for i in peoples:
        infection[temp.index(i)] = 'No'

for i in infection:
    print(i)