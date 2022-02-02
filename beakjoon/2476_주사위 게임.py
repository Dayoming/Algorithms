t = int(input())
reward = list()

for i in range(t):
    dice = list(map(int, input().split()))
    count = {}

    for j in dice:
        try: count[j] += 1
        except: count[j] = 1

    if len(count) == 3:
        reward.append(max(count) * 100)
    elif len(count) == 2:
        reverse_dict = dict(map(reversed, count.items()))
        reward.append(1000 + int(reverse_dict[2]) * 100)
    elif len(count) == 1:
        reward.append(10000 + dice[0] * 1000)

reward.sort(reverse=True)
print(reward[0])