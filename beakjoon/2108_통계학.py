# 왜 시간초과가 날까?

import sys

t = int(sys.stdin.readline())
temp = []
result = []
cnt = []
sum = 0

for i in range(t):
    n = int(sys.stdin.readline())
    temp.append(n)
    sum = sum + n

# 산술평균 구하기
print(round(sum / t)) 

# 중앙값 구하기
median_temp = list(temp) 
median_temp.sort()
print(median_temp[t // 2]) # 중앙값 출력

# 최빈값 구하기
for j in temp: 
    cnt.append(temp.count(j))

mode_temp = list(temp)
mode_value = max(cnt) # 최빈값 수

if cnt.count(mode_value) > 1: # 최빈값이 2개 이상이면 두 번째로 작은 값 출력
    for k in cnt:
        if k < mode_value: # 최빈값이 아닌 수를 리스트에서 제거
            del mode_temp[cnt.index(k)]
            del cnt[cnt.index(k)]
    mode_set = set(mode_temp) # set을 이용해 중복 제거
    mode_temp = list(mode_set)
    mode_temp.sort()
    print(mode_temp[cnt.index(mode_value) + 1]) # 두 번째로 작은 값 출력
else:
    print(temp[cnt.index(mode_value)]) # 아니면 최빈값 출력
print(max(temp) - min(temp)) # 범위 출력