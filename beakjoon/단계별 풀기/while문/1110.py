# 더하기 사이클

n = int(input())

if n < 10:
    a = 0
    b = n
else:
    a = int(n / 10)
    b = int(n % 10)

temp = 0
count = 0

while True:

    if temp == n and n != 0:
        break
    elif n == 0:
        count = 1
        break

    temp = a + b

    if temp >= 10:
        temp = b * 10 + int(temp % 10)
    else:
        temp = b * 10 + temp

    a = int(temp / 10)
    b = int(temp % 10)
    
    count = count + 1

print(count)