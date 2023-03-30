import sys

n = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))

solution.sort()

left = 0
right = len(solution) - 1
minimum = solution[left] + solution[right]

while left < right:
    sum_s = solution[left] + solution[right]
    # 만약 현재 포인터로 선택된 용액 특성값 합의 절대값이 현재까지 최소 특성값보다 작거나 같으면
    if abs(sum_s) <= abs(minimum):
        # 만약 두 용액의 합이 0이면, 바로 정답을 출력하고 반복 종료
        if sum_s == 0:
            print(sum_s)
            break
        # 그렇지 않다면 최소 특성값 minimum을 선택된 용액 특성값 합으로 갱신
        minimum = sum_s

    if sum_s > 0:
        right -= 1
    elif sum_s < 0:
        left += 1

print(minimum)