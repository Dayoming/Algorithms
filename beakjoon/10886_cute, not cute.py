n = int(input())
opinion = []

for i in range(n):
    opinion.append(input())

if opinion.count('1') > opinion.count('0'):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')