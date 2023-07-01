n, m = map(int, input().split())
plates = list(input().split())
prices = list(input().split())
p = list(map(int, input().split()))
answer = 0

prices_dict = dict()

# 딕셔너리에 접시에 맞는 값 넣기
for i in range(len(prices)):
    prices_dict[prices[i]] = p[i + 1]

# 접시 색에 맞는 값만큼 더하고, 해당하지 않으면 P[0]을 더함
for i in range(len(plates)):
    if plates[i] in prices:
        answer += prices_dict[plates[i]]
    else:
        answer += p[0]

print(answer)