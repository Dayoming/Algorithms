# 두 포인터
import sys

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

left = 0
right = 1
temp = numbers[0]
answer = []

# 주어진 수열이 하나이면서 s 이상인 경우 1 출력
if len(numbers) == 1 and temp >= s:
    print(1)
    exit()

while left <= right:
    # 만약 부분합이 s 이상이면 길이 저장 후 temp에서 값 빼주기
    if temp >= s:
        answer.append(right - left)
        temp -= numbers[left]
        left += 1
    # 만약 부분합이 s보다 작으면 temp에 값 더해주기
    elif temp < s:
        if right == n:
            break
        temp += numbers[right]
        right += 1
     # 오른쪽 포인터가 리스트의 마지막에 도달하면 종료

if answer:
    print(min(answer))
else:
    print(0)