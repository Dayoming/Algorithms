# 예제 4-2 시각
# 완전 탐색
# 완전 탐색은 일반적으로 확인해야 할 전체 데이터의 개수가 100만 개 이하일 때 적합
N = int(input())

count = 0
# 시간
for i in range(N + 1):
    # 분
    for j in range(60):
        # 초
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
