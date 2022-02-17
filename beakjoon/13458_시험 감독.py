import sys
input = sys.stdin.readline
 
n = int(input()) # 시험장 개수
students = list(map(int, input().split())) # 시험장 당 응시자의 수
first, second = map(int, input().split()) # 총감독관이 감시하는 수, 부감독관이 감시하는 수
 
cnt = 0
 
for student in students:
    if student - first > 0: # 총감독관은 한 명만
        student -= first
        cnt += 1
        while student > 0: # 나머지는 부감독관이
            student -= second
            cnt += 1
    else:
        while student > 0: # 총감독관이 한 명도 필요하지 않으면
            student -= second
            cnt += 1
 
print(cnt)