dice = list(map(int, input().split()))
count = {} # 주사위 눈당 나온 개수를 저장할 딕셔너리

for i in dice: # 각각 count를 저장
    try: count[i] += 1 # 있으면 += 1 실행
    except: count[i] = 1 # 없는 키값이면 1을 저장

if len(count) == 3: # 각각 다 다른 눈이면
    print(max(count) * 100) # (가장 큰 눈) * 100
elif len(count) == 2: # 같은 눈이 2개만 나오는 경우
    reverse_dict = dict(map(reversed, count.items())) # key와 value값을 뒤집음
    print(1000 + int(reverse_dict[2]) * 100) # 1000 + (같은 눈) * 100
elif len(count) == 1: # 모두 같은 눈인 경우
    print(10000 + dice[0] * 1000) # 10000 + (같은 눈) * 1000