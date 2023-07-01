n = list(map(int, input().split()))

temp = n[0]
answer = 'Yes'

for i in range(1, len(n)):
    # 증가해야 하고, 100부터 675 사이여야 하며, 25의 배수여야 함
    if temp <= n[i] and n[i] >= 100 and n[i] <= 675 and n[i] % 25 == 0:
        temp = n[i]
    else:
        answer = 'No'

print(answer)