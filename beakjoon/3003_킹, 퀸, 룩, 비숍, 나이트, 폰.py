white_piece = list(map(int, input().split()))

black_piece = [1, 1, 2, 2, 2, 8]
result = []

for i in range(len(white_piece)):
    result.append(black_piece[i] - white_piece[i])

print(*result)
