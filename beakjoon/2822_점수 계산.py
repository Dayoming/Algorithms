scores = dict()
solved = []
sum_score = 0

for i in range(1, 9):
    scores[i] = int(input())

scores = sorted(scores.items(), key = lambda x:x[1], reverse=True)

for i, j in scores[0:5]:
    solved.append(i)
    sum_score += j

solved.sort()

print(sum_score)
print(*solved)