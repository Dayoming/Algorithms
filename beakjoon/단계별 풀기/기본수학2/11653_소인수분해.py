n = int(input())
m = 2
while n != 1: # 몫이 1일때 멈춘다
    if n % m == 0:
        print(m)
        n = n // m
    else:
        m = m + 1