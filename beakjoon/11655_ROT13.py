s = input()

for i in s:
    check = ord(i)
    if check >= 65 and check <= 90: # 대문자인 경우
        if check + 13 > 90:
            check = 64 + (check + 13) - 90
        else:
            check = check + 13
        print(chr(check), end='')
    elif check >= 97 and check <= 122: # 소문자인 경우
        if check + 13 > 122:
            check = 96 + (check + 13) - 122
        else:
            check = check + 13
        print(chr(check), end='')
    else:
        print(i, end='')