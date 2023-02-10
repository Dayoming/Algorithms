# 동전 0
# 그리디 알고리즘
import sys

n, money = map(int, sys.stdin.readline().split())
coins = []
cnt = 0

for i in range(n):
    # 수를 입력받고, 만약 가치의 합 보다 크면 제외
    temp = int(sys.stdin.readline())
    if temp <= money:
        coins.append(temp)

# 역순으로 정렬
coins.reverse()

for j in range(n):
    # 만약 지금 갖고 있는 돈에서 현재 검사할 동전 값을 뺀 결과가 0보다 크거나 같다면
    if money - coins[j] >= 0:
        # 필요한 동전 수에 돈을 동전으로 나눈 몫을 더해준다.
        # ex) 1200 // 1000 = 1 -> 1000원짜리 1개
        cnt += money // coins[j]
        # 지금 갖고 있는 돈은 동전으로 나눈 나머지로 할당한다.
        money = money % coins[j]
    # 갖고 있는 돈이 0원이 되면 종료한다.
    if money == 0:
        break

print(cnt)