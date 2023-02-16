# 구현, 자료 구조, 큐
import sys
from collections import deque

n = int(sys.stdin.readline())
cards = deque([i for i in range(1, n + 1)])

while len(cards) != 1:
    print(cards.popleft(), end=' ')
    cards.append(cards.popleft())

print(cards[0])
