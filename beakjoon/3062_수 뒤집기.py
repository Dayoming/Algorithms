t = int(input())

while t > 0:
    n = input()
    temp = n[::-1] # list[start : end : step] 슬라이싱, 전체를 거꾸로 가져옴

    sum = int(n) + int(temp)

    if str(sum) == str(sum)[::-1]:
        print('YES')
    else:
        print('NO')
    t = t - 1