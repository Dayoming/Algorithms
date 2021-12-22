# 단어 공부
# 고친 코드

s = input().upper()
alphabet = list(set(s))
count_arr = []

for i in alphabet:
    count_arr.append(s.count(i))

if count_arr.count(max(count_arr)) > 1:
    print('?')
else:
    max_count = count_arr.index(max(count_arr))
    print(alphabet[max_count])