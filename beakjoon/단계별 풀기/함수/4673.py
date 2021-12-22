# 셀프 넘버

def self_number(n):
    num = n
    while n != 0:
        num = int(num + n % 10)
        n = int(n / 10)
    return num

d = [True for i in range(10000)]

for i in range(1, 10001):
    not_self = self_number(i)
    if not_self < 10000:
        d[not_self] = False

for i in range(1, 10000):
    if d[i] == True:
        print(i)
