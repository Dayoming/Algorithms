t = int(input())

for test_case in range(1, t + 1):
    memory = list(input())
    modify = list('0' for i in range(len(memory)))
    count = 0

    for i in range(len(memory)):
        if memory == modify:
            break
        if memory[i] == '1' and modify[i] == '0':
            for j in range(i, len(modify)):
                modify[j] = '1'
            count += 1
        if memory[i] == '0' and modify[i] == '1':
            for j in range(i, len(modify)):
                modify[j] = '0'
            count += 1
    print("#{} {}".format(test_case, count))
