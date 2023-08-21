t, s = map(int, input().split())

# 점심 식사이면서 술과 같이 먹지 않을 때는 320개
if (t >= 12 and t <= 16) and s == 0:
    print(320)
# 술하고 같이 초밥을 먹거나, 점심 식사가 아닐 때는 280개
elif s == 1 or (t < 12 or t > 16):
    print(280)