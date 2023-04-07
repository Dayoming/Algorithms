dwarfs = list()
check = False

for _ in range(9):
    dwarf = int(input())
    dwarfs.append(dwarf)

temp = sum(dwarfs)

for i in range(len(dwarfs)):
    for j in range(i + 1, len(dwarfs)):
        if temp - (dwarfs[i] + dwarfs[j]) == 100:
            del dwarfs[j]
            del dwarfs[i]
            check = True
            break
    if check:
        break
            
dwarfs.sort()

for i in dwarfs:
    print(i)
