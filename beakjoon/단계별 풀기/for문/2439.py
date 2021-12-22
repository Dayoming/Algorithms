# 별 찍기 - 2
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#     *
#    **
#   ***
#  ****
# *****

n = int(input())
temp = n - 1

for i in range(n):
    for j in range(n):
        if j < temp:
            print(" ", end = '')
        elif j >= temp:
            print("*", end = '')
    print()
    temp = temp - 1
