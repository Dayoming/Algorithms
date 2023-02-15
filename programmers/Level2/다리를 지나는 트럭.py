# 스택/큐 - 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 걸리는 시간
    answer = 0
    # 대기 중인 트럭
    trucks = deque(truck_weights)
    # 다리를 건너고 있는 중인 트럭
    bridge = deque([0] * bridge_length)
    # 다리를 건너고 있는 중인 트럭 무게의 합
    bridge_weight = 0

    while bridge:
        bridge_weight -= bridge.popleft()
        # 대기중인 트럭이 존재하면
        if trucks:
            # 만약 다리를 건너는 중인 트럭 무게 + 다리를 건널 트럭 무게가 무게 제한보다 작다면
            if bridge_weight + trucks[0] <= weight:
                truck_weight = trucks.popleft()
                # 다리에 트럭 한 대를 더해준다
                bridge.append(truck_weight)
                # 다리를 건너고 있는 중인 트럭 무게의 합에 트럭 무게를 더해준다
                bridge_weight += truck_weight
            else:
                # 제한보다 크다면 0을 추가해 다리 길이를 유지한다
                bridge.append(0)
        answer += 1

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
