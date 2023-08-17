import sys

moeum = ['a', 'e', 'i', 'o', 'u']

while True:
    s = sys.stdin.readline().rstrip()
    cnt = 0
    if s == '#':
        break
    
    s = s.lower()
    
    for i in s:
        if i in moeum:
            cnt += 1
    
    print(cnt)