# 스택/큐 - 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 걸리는 시간
    answer = 0
    # 대기 중인 트럭
    trucks = deque(truck_weights)
    # 다리를 건너고 있는 중인 트럭
    bridge = deque()
    # 다리를 건너고 있는 중인 트럭 무게의 합
    bridge_weight = 0

    while trucks:
        if bridge_weight <= weight:
            if bridge_weight + trucks[0] <= weight:
                truck_weight = trucks.popleft()
                bridge.append(truck_weight)
                bridge_weight += truck_weight
                answer += 1
            else:
                bridge_weight -= bridge.popleft()
                answer += 1

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
