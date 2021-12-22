# 최장 증가 부분 수열(LIS) 알고리즘
# https://alpyrithm.tistory.com/91
# https://pacific-ocean.tistory.com/212

n = int(input())
box = list(map(int, input().split()))
dp = [1 for _ in range(n)] # 리스트 1로 n개만큼 초기화

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]: # 뒤에 있는 상자가 앞의 상자보다 크면
            dp[i] = max(dp[i], dp[j] + 1) # 큰 값을 dp에 저장
print(max(dp))