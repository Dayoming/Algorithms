# 나이순 정렬
n = int(input())
member_list = []

for i in range(n):
    age, name = input().split()
    member_list.append([int(age), name])

# 각 회원을 나이 순으로 정렬
member_list.sort(key=lambda member_list: member_list[0])

for i in range(0, n):
    print(member_list[i][0], member_list[i][1])