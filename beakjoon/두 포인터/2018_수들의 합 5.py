import sys

n = int(sys.stdin.readline())

left = 0
right = 1
# 가지수 저장
answer = 1
temp = 0

while left < right:
    if right > n:
        break
    
    if temp < n:
        temp += right
        right += 1
    elif temp > n:
        left += 1
        temp -= left
    elif temp == n:
        answer += 1
        left += 1
        temp -= left

print(answer)