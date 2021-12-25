n = int(input())
firstFile = list(input())
firstFileLen = len(firstFile)

for i in range(n - 1):
    otherFile = list(input())

    for j in range(firstFileLen):
        if firstFile[j] != otherFile[j]:
            firstFile[j] = "?"

print(''.join(firstFile))