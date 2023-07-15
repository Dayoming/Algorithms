n = int(input())
strings = set()
count = 0

for _ in range(n):
    s = input()
    if s not in strings and s[::-1] not in strings:
        strings.add(s)
    else:
        count += 1

print(n - count)