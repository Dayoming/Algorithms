from itertools import combinations


n, m = map(int, input().split())
cards = list(map(int, input().split()))
s = list(combinations(cards, 3))
result = 0

for i in s:
    card_sum = i[0] + i[1] + i[2]
    if card_sum <= m and card_sum > result:
        result = card_sum

print(result)
