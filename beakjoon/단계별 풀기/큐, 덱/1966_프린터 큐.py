import sys
from collections import deque

# 테스트케이스의 수
t = int(sys.stdin.readline())

for i in range(t):
    # 문서의 개수 N, 몇 번째로 인쇄되었는지 궁금한 문서의 위치 M -> 인덱스로 사용
    n, m = map(int, sys.stdin.readline().split())
    importance = deque(map(int, sys.stdin.readline().split()))
    cnt = 0

    while importance:
        best = max(importance) # 최댓값 저장
        front = importance.popleft() # 큐에서 가장 앞의 요소를 뽑음
        m -= 1 # 하나 뽑았으므로 감소

        if best == front: # 만약 최댓값과 가장 앞의 요소값이 같으면
            cnt += 1 # 프린트되므로 cnt 1 증가
            if m < 0: # m이 0보다 작다면 cnt를 출력
                print(cnt)
                break
        else: # 최댓값과 가장 앞의 요소값이 같지 않다면
            importance.append(front) # 가장 앞의 요소를 가장 뒤로 재배치
            if m < 0: # m이 음수라면 큐의 가장 마지막으로 이동
                m = len(importance) - 1

