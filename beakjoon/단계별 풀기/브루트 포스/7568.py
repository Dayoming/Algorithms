# Save the weight, height you have entered
body = []
# Save the rank
rank = []

n = int(input())
for i in range(n):
    weight, height = map(int, input().split())
    body.append((weight, height))

for i in range(n):
    # Save the number of people who are bigger than me
    cnt = 0
    for j in range(n):
        # If wieght, height bigger than me
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            cnt += 1
    rank.append(cnt + 1)

print(*rank)
