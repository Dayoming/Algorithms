s = input()
alphabet = [0 for _ in range(26)]

for i in s:
    alphabet[ord(i) - 97] += 1

print(*alphabet)