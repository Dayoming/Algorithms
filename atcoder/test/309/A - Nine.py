A, B = map(int, input().split())
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flag = 'No'

for i in numbers:
    if A in i and B in i:
        flag = 'Yes'
        break

print(flag)