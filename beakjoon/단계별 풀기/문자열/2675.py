# 문자열 반복

t = int(input())
result = []
temp = ''

for i in range(t):
    t_case = input().split()

    for k in t_case[1]:
        temp = temp + k * int(t_case[0])
    
    result.append(temp)
    temp = ''

for i in result:
    print(i)
