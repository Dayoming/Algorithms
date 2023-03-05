N = int(input())
solution = list(map(int, input().split()))

solution.sort()

left = 0
right = len(solution) - 1

min = abs(solution[left] + solution[right])
answer = []

while left < right:
    sum_s = solution[left] + solution[right]

    if abs(sum_s) <= min:
        if sum_s == 0:
            answer = [solution[left], solution[right]]
            break
        min = abs(sum_s)
        answer = [solution[left], solution[right]]
    if sum_s < 0:
        left += 1
    elif sum_s > 0:
        right -= 1

print(*answer)