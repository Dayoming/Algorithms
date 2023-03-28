# 두 용액
import sys

n = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))

# 용액 특성값 오름차순 정렬
solution.sort()

# 왼쪽 포인터
left = 0
# 오른쪽 포인터
right = len(solution) - 1
# 가장 작은 값을 저장할 변수
min = abs(solution[left] + solution[right])
answer = []

while left < right:
    sum_s = solution[left] + solution[right]
    # 두 수를 더한 절댓값이 지금까지 가장 작은 값보다 작거나 같은 경우
    if abs(sum_s) <= min:
        # 더한 값이 0이면 두 수를 정답에 저장하고 반복문을 빠져나온다.
        if sum_s == 0:
            answer = [solution[left], solution[right]]
            break
        # 가장 작은 값을 바꾼다.
        min = abs(sum_s)
        # 정답 리스트에 해당 값 저장
        answer = [solution[left], solution[right]]
    # 만약 더한 값이 0보다 작다면 더 큰 수를 더해야 하므로 왼쪽 포인터 + 1
    if sum_s < 0:
        left += 1
    # 만약 더한 값이 0보다 크다면 더 작은 수를 더해야 하므로 오른쪽 포인터 - 1
    elif sum_s > 0:
        right -= 1

print(*answer)