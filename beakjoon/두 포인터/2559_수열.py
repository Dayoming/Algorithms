n, k = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
right = 1
maximum = -99999999
sum_t = numbers[left]

if k == 1:
    print(max(numbers))
    exit(0)

while left <= right and right < n:
    sum_t += numbers[right]
    
    # 만약 연속적인 정도가 k와 같다면
    if right - left == k - 1:
        # 만약 누적된 합이 현재까지 최대값보다 크다면 최대값 갱신
        if sum_t > maximum:
            maximum = sum_t
        # 누적값에서 가장 왼쪽 값을 빼주고, 범위를 한 칸씩 오른쪽으로 옮긴다
        sum_t -= numbers[left]
        left += 1
        right += 1
    # 연속적인 정도가 k가 될 때까지 오른쪽으로 범위 확장
    else:
        right += 1
               

print(maximum)