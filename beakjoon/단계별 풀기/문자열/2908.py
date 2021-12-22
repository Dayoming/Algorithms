# 상수

a, b = map(str, input().split())
rev_a = []
rev_b = []
result_a = 0
result_b = 0
temp = -1

for i in range(3):
    rev_a.append(a[temp])
    rev_b.append(b[temp])
    temp = temp - 1

temp = 100
for i in range(3):
    result_a = result_a + int(rev_a[i]) * temp
    result_b = result_b + int(rev_b[i]) * temp
    temp = temp / 10

if result_a > result_b:
    print(int(result_a))
else:
    print(int(result_b))