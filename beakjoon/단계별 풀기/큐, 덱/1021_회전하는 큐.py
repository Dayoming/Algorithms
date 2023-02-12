# 자료구조 - 덱
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
idxs = list(map(int, sys.stdin.readline().split()))
# 값은 상관 없으므로 각각 위치로 리스트 초기화
numbers = deque([i for i in range(1, n + 1)])

cnt = 0

for idx in idxs:
    while True:
        # 만약 순환 큐의 가장 첫 번째 원소가 찾으려는 위치와 같으면
        if numbers[0] == idx:
            # 첫 번째 원소를 뽑아내고 멈춘다
            numbers.popleft()
            break
        else:
            # 그렇지 않을 때, 만약 순환 큐의 찾으려는 위치가 순환 큐의 길이의 절반보다 작다면
            if numbers.index(idx) < len(numbers) / 2:
                # 순환 큐의 첫 번째 원소가 찾으려는 위치가 아닌 동안
                while numbers[0] != idx:
                    # 순환 큐를 왼쪽으로 한 칸 이동시킨다.
                    numbers.append(numbers.popleft())
                    cnt += 1
            else:
                # 찾으려는 위치가 순환 큐의 절반보다 크면
                while numbers[0] != idx:
                    # 순환 큐를 오른쪽으로 한 칸 이동시킨다.
                    numbers.appendleft(numbers.pop())
                    cnt += 1

print(cnt)
