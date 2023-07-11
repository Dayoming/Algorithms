# 이동하려고 하는 채널
n = int(input())
# 고장난 버튼의 개수
m = int(input())

# 고장난 버튼이 있는 경우
if m:
    buttons = list(input().split())
else:
    buttons = []

# 예를 들어 이동하려고 하는 채널이 1000이면, 리모콘의 + 버튼으로 이동할 수 있는 최대 숫자는 900번이다
# 10이면, 리모콘의 - 버튼으로 이동할 수 있는 최대 숫자는 90번이다
count = abs(n - 100)
# 고장나지 않은 버튼들로 만들 수 있는 숫자인지 판별하는 변수
flag = True

# 큰 수에서 작은 수로, 작은 수에서 큰 수 두 구간 탐색
for i in range(1000001):
    x = list(str(i))
    # flag 초기화
    flag = True
    
    for c in x:
        # 이동하려는 채널 요소에 고장난 버튼이 들어있을 경우
        if c in buttons:
            flag = False

    # 만약 리모콘의 숫자로 만들 수 있는 수라면,
    # 현재 count(+와 -로 이동할 수 있는 가장 큰 수),
    # (현재 수의 길이 + n - i의 절대값) 중 작은 수를 count에 저장
    if flag == True:
        count = min(count, len(str(i)) + abs(n - i))
    
print(count)