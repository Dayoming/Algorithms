# 카드2
import sys
from collections import deque

n = int(sys.stdin.readline())
cards = deque([i for i in range(1, n + 1)])

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])

