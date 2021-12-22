A = input()
B = input()
temp = []

for i in B:
    temp.append(i)

temp.reverse()

for j in temp:
    result = int(A) * int(j)
    print(result)

print(int(A) * int(B))