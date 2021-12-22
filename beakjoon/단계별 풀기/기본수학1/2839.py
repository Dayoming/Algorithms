# 설탕 배달

n = int(input())
box = 0

while True:
    if n % 5 == 0:
        box = box + n / 5
        print(int(box))
        break
    n = n - 3
    box = box + 1
    if n < 0:
        print('-1')
        break