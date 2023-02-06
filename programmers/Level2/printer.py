# 스택/큐 - 프린터
from collections import deque

def solution(priorities, location):
    # 포인터로 사용할 변수
    pointer = location
    importance = deque(priorities)
    cnt = 0

    # 대기열이 존재하는 동안
    while importance:
        # 큐에서 가장 높은 중요도 값을 저장
        best = max(importance)
        front = importance.popleft()
        # 큐에서 하나 뽑았으므로 감소
        pointer -= 1

        # 중요도 값이 가장 큰 것과 같으면
        if best == front:
            cnt += 1
            if pointer < 0: # pointer가 0보다 작다면 cnt를 출력
                return cnt
        else: # 최댓값과 가장 앞의 요소값이 같지 않다면
            importance.append(front) # 가장 앞의 요소를 가장 뒤로 재배치
            if pointer < 0: # pointer가 음수라면 큐의 가장 마지막으로 이동
                pointer = len(importance) - 1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))