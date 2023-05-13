n = int(input())
s = input()

Takahashi = 0
Aoki = 0

for i in s:
    if i == 'A':
        Aoki += 1
    else:
        Takahashi += 1

if Takahashi > Aoki:
    print('T')
elif Takahashi < Aoki:
    print('A')
elif Takahashi == Aoki:
    if s[-1] == 'A':
        print('T')
    else:
        print('A')