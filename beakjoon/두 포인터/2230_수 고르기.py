import sys

n, m = map(int, sys.stdin.readline().split())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

left = 0
right = 1
min = int(2e9)

while left <= right and right < n:
    temp = numbers[right] - numbers[left]

    # 만약 차이가 m 이상이면
    if temp > m:
        # 차이가 현재 최소값보다 작으면 최소값 갱신
        if temp < min:
            min = temp
        left += 1
    # 만약 차이가 m보다 작으면
    elif temp < m:
        right += 1
    elif temp == m:
        print(temp)
        exit(0)

print(min)
