x, y, w, h = map(int, input().split())

# 위, 아래, 왼쪽, 오른쪽 중 가장 작은 수
print(min(x, h - y, y, w - x))