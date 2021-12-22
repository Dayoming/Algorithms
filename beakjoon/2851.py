temp = [] # 버섯 점수 담을 배열 선언
result = 0 # 누적 점수 저장할 변수 선언

for i in range(10): # 버섯 점수 저장
    temp.append(int(input()))

for j in temp:
    result = result + j # 점수 누적

    if result >= 100:
        if result - 100 > 100 - (result - j): # 현재 누적값에서 100을 뺀 값과 100에서 이전 누적값을 뺀 값을 비교
            result = result - j # 차이가 더 크다면 이전 값으로 돌려준다
        break

print(result)