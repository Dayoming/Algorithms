# OX퀴즈

n = int(input())
result = []
count = 0
temp = 0

for i in range(n):
    t_case = input()
    for j in range(len(t_case)):
        if t_case[j] == 'O':
            count = count + 1
            temp = temp + count
        else:
            count = 0

    result.append(temp)
    temp = 0
    count = 0

for i in result:
    print(i)
