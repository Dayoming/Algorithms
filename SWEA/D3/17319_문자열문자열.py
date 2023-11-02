tc = int(input())

for case in range(1, tc + 1):
    n = int(input())
    s = input()
    result = "No"
    
    # 문자열이 짝수이고, 반으로 나눴을 때 두 문자열이 같으면 Yes
    if len(s) % 2 == 0:
        if s[0:len(s) // 2] == s[len(s) // 2::]:
            result = "Yes"
    
    print("#{} {}".format(case, result))