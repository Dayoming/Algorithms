import sys

# 반올림 사사오입 함수    
def customRound(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(sys.stdin.readline())
difficulty = []

# 아직 아무 의견이 없다면 문제의 난이도는 0
if n == 0:
    print(0)
    exit(0)
    
for _ in range(n):
    difficulty.append(int(sys.stdin.readline()))
    
# 의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균
# 위에서 얼마, 아래에서 얼마를 절사해야 하는지 결정
difficulty.sort()
exclusion = customRound(n * 0.15)

del difficulty[0:exclusion]
del difficulty[len(difficulty) - exclusion:n]

print(customRound(sum(difficulty) / len(difficulty)))