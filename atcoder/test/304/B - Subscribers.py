
n = int(input())

# 만약 N이 10^3 - 1보다 작거나 같으면 N을 있는 그대로 출력
# 만약 N이 10^3와 10^4 - 1 사이이면, 일의 자리와 그 아래 모든 숫자를 잘라서 줄력
# 만약 N이 10^4와 10^5 - 1 사이이면, 십의 자리와 그 아래 모든 숫자를 잘라서 출
# 만약 N이 10^5와 10^6 - 1 사이이면, 백의 자리와 그 아래 모든 숫자를 잘라서 줄력
# 만약 N이 10^6와 10^7 - 1 사이이면, 천의 자리와 그 아래 모든 숫자를 잘라서 줄력
# 만약 N이 10^7와 10^8 - 1 사이이면, 만의 자리와 그 아래 모든 숫자를 잘라서 줄력
# 만약 N이 10^8와 10^9 - 1 사이이면, 십만의 자리와 그 아래 모든 숫자를 잘라서 줄력

if n >= 1000 and n <= 9999:
    answer = str(n)[0:3] + '0'
elif n >= 10000 and n <= 99999:
    answer = str(n)[0:3] + '00'
elif n >= 100000 and n <= 999999:
    answer = str(n)[0:3] + '000'
elif n >= 1000000 and n <= 9999999:
    answer = str(n)[0:3] + '0000'
elif n >= 10000000 and n <= 99999999:
    answer = str(n)[0:3] + '00000'
elif n >= 100000000 and n <= 999999999:
    answer = str(n)[0:3] + '000000'
else:
    answer = n

print(answer)