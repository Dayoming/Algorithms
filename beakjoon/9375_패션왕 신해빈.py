t = int(input())

for _ in range(t):
    n = int(input())
    wear = dict()
    for _ in range(n):
        clothes, kind = input().split()
        if kind in wear:
            wear[kind].append(clothes)
        else:
            wear[kind] = [clothes]
    cnt = 1
    
    for i in wear:
        cnt *= (len(wear[i])+1)
    
    print(cnt - 1)
        