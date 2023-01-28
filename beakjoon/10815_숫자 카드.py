# 숫자 카드
import sys

# 이분 탐색
def binary_search(target, data):
    left = 0
    right = len(have_cards) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

n = int(sys.stdin.readline())
have_cards = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

result = []

have_cards.sort()

for i in range(m):
    result.append(binary_search(cards[i], have_cards))

print(*result)