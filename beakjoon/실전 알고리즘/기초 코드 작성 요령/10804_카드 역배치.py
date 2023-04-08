cards = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    idx_a = a - 1
    idx_b = b - 1
    if b - a == 1:
        temp = cards[idx_a]
        cards[idx_a] = cards[idx_b]
        cards[idx_b] = temp
    elif idx_a - 1 < 0:
        cards[idx_a:b] = cards[idx_b::-1]
    else:
        cards[idx_a:b] = cards[idx_b:idx_a - 1:-1]

print(*cards)