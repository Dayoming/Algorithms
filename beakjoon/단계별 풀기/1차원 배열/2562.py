# 최댓값
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

result = []
count = 1
temp = 0

for i in range(9):
    n = int(input())
    result.append(n)

for j in range(len(result)):
    if result[j] > temp:
        temp = result[j]
        count = j + 1

print(temp)
print(count)