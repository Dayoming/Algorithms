import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

numbers.sort()

left = 0
right = len(numbers) - 1
answer = 0

while left < right:
    temp = numbers[left] + numbers[right]
    
    if temp < x:
        left += 1
    elif temp > x:
        right -= 1
    elif temp == x:
        answer += 1
        left += 1

print(answer)