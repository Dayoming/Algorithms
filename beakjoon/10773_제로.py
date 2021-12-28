k = int(input())
nlist = []
result = 0

for i in range(0, k):
    n = int(input())
    if n == 0:
        del nlist[len(nlist) - 1]    
    else:
        nlist.append(n)

for j in nlist:
    result = result + j

print(result)
    