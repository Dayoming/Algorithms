# 이분 탐색
import sys

K, N = map(int, sys.stdin.readline().split())
lines = []

for _ in range(K):
    lines.append(int(sys.stdin.readline()))

# K개의 랜선을 잘라서 모두 N개의 같은 길이의 랜선으로 만들고 싶음
# 예를 들어 300cm 짜리 랜선에서 140cm짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다
# 이미 자른 랜선은 붙일 수 없음
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함
# 만들 수 있는 최대 랜선의 길이
result = 0

start = 0
end = max(lines)

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    if mid == 0:
        result = end
        break

    for i in lines:
        if i != 0:
            cnt += i // mid
    
    # 자른 랜선의 개수가 필요한 랜선의 개수보다 작으면
    if cnt < N:
        end = mid - 1 # 더 작게 잘라야 한다
    else:
        # 자른 랜선의 개수가 필요한 랜선의 개수보다 크거나 같으면
        result = mid # 현재 자른 랜선의 길이를 저장하고
        start = mid + 1 # 더 크게 잘라본다(최대 랜선)

print(result)