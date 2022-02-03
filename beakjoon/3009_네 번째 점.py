x_list = []
y_list = []

for i in range(0, 3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(0, 3): # 각각 리스트에서 짝이 없는 수를 찾는다
    if x_list.count(x_list[i]) == 1:
        x4 = x_list[i]
    elif y_list.count(y_list[i]) == 1:
        y4 = y_list[i]

print(x4, y4)