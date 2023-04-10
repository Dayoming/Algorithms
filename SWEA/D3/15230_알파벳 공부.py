T = int(input())

alphabet = list('abcdefghijklmnopqrstuvwxyz')

for test_case in range(1, T + 1):
    string = list(input())
    count = 0

    for i in range(len(string)):
        if string[i] == alphabet[i]:
            count += 1
        else:
            break

    print("#{} {}".format(test_case, count))