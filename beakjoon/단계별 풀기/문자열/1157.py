# 단어 공부
# 시간 초과

s = input().lower()
alphabet = list(s)
count_arr = []

for i in alphabet:
    count_arr.append(s.count(i))

max_num = max(count_arr)
max_s = alphabet[count_arr.index(max_num)]

for i in range(len(alphabet)):
    if count_arr[i] == max_num and alphabet[i] == max_s:
        pass
    elif count_arr[i] == max_num and alphabet[i] != max_s:
        max_s = '?'
        break

print(max_s.upper())