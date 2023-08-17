from itertools import product

a, b = map(int, input().split())
a_digits = list(map(int, str(a)))
b_digits = list(map(int, str(b)))
answer = 0

for com in product(a_digits, b_digits):
    answer += com[0] * com[1]

print(answer)
