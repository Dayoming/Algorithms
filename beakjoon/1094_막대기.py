x = int(input())
# 주어진 막대가 64cm이고 반으로 계속해서 나눈다고 했을 때 나올 수 있는 경우의 수
stick = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(stick)):
    # 막대의 길이가 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다.
    if x >= stick[i]:
        count += 1
        x -= stick[i]
    # X가 0이 되면 종료한다.
    if x == 0:
        break

print(count)