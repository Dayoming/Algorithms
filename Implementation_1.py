# 예제 4-1 상하좌우
N = int(input())
plan = list(input().split())

x = 1
y = 1

for cmd in plan:
    if cmd == 'R' and x < N:
        x += 1
    elif cmd == 'L' and x > 1:
        x -= 1
    elif cmd == 'U' and y > 1:
        y -= 1
    elif cmd == 'D' and y < N:
        y += 1
    
print(y, x)