# 숫자 카드 게임
N, M = map(int, input().split())

result = 0

for i in range(N):
    data = list(map(int, input().split()))
    # 입력받은 리스트 중에서 가장 작은 수를 구한다
    min_value = min(data)
    # 현재 result와 입력받은 리스트에서 가장 작은 수 중 큰 수를 선택해서 저장한다
    result = max(result, min_value)

print(result)