import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

left = 0
right = 1
temp = 0
answer = 0

while left <= right:
    if right > len(numbers):
        break

    temp = sum(numbers[left:right])

    if temp < m:
        right += 1
    elif temp > m:
        left += 1
    elif temp == m:
        answer += 1
        left += 1

print(answer)