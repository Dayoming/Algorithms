t = int(input())
for i in range(t):
    n = int(input())
    school = {}
    for j in range(n):
        name, alcohol = input().split()
        school[name] = int(alcohol)
    max_key = max(school, key=school.get) # max(iterable, key=dict.get) 을 통해 value 값 중 가장 큰 값 찾기
    print(max_key)