# 개수 세기
n = int(input())
numbers = map(int, input().split())
v = int(input())
cnt = 0

for i in numbers:
    if i == v:
        cnt += 1

print(cnt)