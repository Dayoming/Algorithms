# 평균은 넘겠지

n = int(input())
temp = 0
count = 0
avg_score = []
result = []


for i in range(n): # 학생 수와 점수를 입력받고, 각 줄의 평균을 구한다.
    score = list(map(int, input().split()))
    for j in range(1, len(score)):
        temp = temp + score[j]
    
    avg_score.append(temp / score[0])
    temp = 0

    for k in range(1, len(score)):
        if avg_score[i] < score[k]:
            count = count + 1
    
    result.append(format(count / score[0] * 100, ".3f") + '%')
    count = 0

for i in result:
    print(i)
