# 알파벳 찾기

s = input()
result = []

for i in range(0, 26):
    if chr(i + 97) in s:
        result.append(str(s.find(chr(i + 97))))
    else:
        result.append('-1')

print(' '.join(result))