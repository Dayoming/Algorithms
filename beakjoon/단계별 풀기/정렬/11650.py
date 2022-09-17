n = int(input())
coordinates = []

# Input coordinates
for i in range(n):
    x, y = map(int, input().split())
    coordinates.append([x, y])

# List sort
coordinates.sort()

# Result print out
for i in coordinates:
    print(i[0], i[1])
