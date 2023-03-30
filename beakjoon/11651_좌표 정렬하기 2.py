n = int(input())
coordinates = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append([x, y])

coordinates = sorted(coordinates, key = lambda x : (x[1], x[0]))

for i in coordinates:
    print(*i)
