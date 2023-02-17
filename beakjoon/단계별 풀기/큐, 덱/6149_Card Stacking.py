# 구현, 자료 구조, 시뮬레이션, 덱, 큐
import sys
from collections import deque

# n - 1명의 친구들과 k장의 카드로 게임
# 한 장 나눠줄 때마다 p장의 카드를 덱 아래로 내려놓아야 함
n, k, p = map(int, sys.stdin.readline().split())
cards = deque([i for i in range(1, k + 1)])
answer = []
cnt = 1

while cards:
    if cnt == n:
        answer.append(cards.popleft())
        cards.rotate(-p)
        cnt = 1
    else:
        cards.popleft()
        cards.rotate(-p)
        cnt += 1

answer.sort()

for i in answer:
    print(i)