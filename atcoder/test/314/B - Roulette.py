n = int(input())
scores = dict()
winner = []

for i in range(1, n + 1):
    # 배팅한 번호의 수
    c = int(input())
    # 배팅한 번호
    score = list(map(int, input().split()))
    scores[i] = score

# 정답 룰렛 번호
x = int(input())

# 정답 번호를 선택하지 않은 사람 삭제
for key in range(1, n + 1):
    if x not in scores[key]:
        scores.pop(key)

if scores:
    min_len = len(min(scores.values(), key=len))

    for key in scores.keys():
        if len(scores[key]) <= min_len:
            winner.append(key)
            
print(len(winner))
print(*winner)