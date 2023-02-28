# 이진 탐색
# 떡볶이 떡 만들기
import sys

# '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 후 조건의 만족 여부('예' 또는 '아니오')에 따라서 탐색 범위를 좁혀서 해결
# 절단기의 높이가 0부터 10억까지의 정수 중 하나, 즉 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 한다
N, M = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
answer = []

# 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기
# 현재 탐색할 수 있는 범위는 0 ~ (h중 가장 큰 수)
# 중간 값으로 잘라서 조건 M을 만족하면 중간 값을 저장하고 left 값을 중간 값 오른쪽으로 옮긴다(범위를 좁힌다)
# 더 이상 중간 값이 조건을 만족하지 않으면 종료 후 조건을 만족한 수들 중 가장 큰 값을 반환한다
h.sort()

left = 0
right = max(h)

result = 0
while left <= right:
    total = 0
    mid = (left + right) // 2

    for i in h:
        if i > mid: # 현재 떡 길이가 중간 값보다 크면
            total += i - mid # 떡을 자르고 total에 더해준다

    if total < M: # 총 합이 M보다 작으면 떡을 더 많이 자르기
        right = mid - 1
    else:
        result = mid # 합이 M보다 크거나 같으면 중간 값을 저장하고
        left = mid + 1 # 떡을 덜 자르기

print(result) # 최종 result 값을 반환한다