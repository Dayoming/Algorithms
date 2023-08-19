n = int(input())
customer = list(map(int, input().split()))
cnt = 0
customer.sort()
seat = dict()

for i in customer:
    if i not in seat:
        seat[i] = 0
    else:
        seat[i] += 1

for key in seat.keys():
    cnt += seat[key]

print(cnt)