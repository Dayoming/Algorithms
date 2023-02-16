# 구현, 자료 구조, 시뮬레이션, 큐
import sys
from collections import deque

# n은 다리를 건너는 트럭의 수, w는 다리 길이, l은 다리의 최대하중
n, w, l = map(int, sys.stdin.readline().split())
trucks = deque(list(map(int, sys.stdin.readline().split())))
bridge = deque([0] * w)
bridge_weight = 0
answer = 0

while bridge:
    # 다리 위 트럭의 무게 총합에서 다리 위 트럭 중 가장 왼쪽에 있는 트럭 무게를 빼준다(건너는 트럭)
    bridge_weight -= bridge.popleft()

    # 만약 대기중인 트럭이 존재하면
    if trucks:
        # 만약 건너는 중인 트럭들 무게 + 대기중인 트럭 중 첫 번째 트럭의 무게의 합이 최대하중보다 낮다면
        if bridge_weight + trucks[0] <= l:
            truck = trucks.popleft()
            bridge.append(truck)
            bridge_weight += truck
        # 그렇지 않으면 다리 길이 유지
        else:
            bridge.append(0)
    answer += 1

print(answer)