t = int(input())
school = {'Yonsei':0, 'Korea':0}
for i in range(t):
    for j in range(0, 9):
        a, b = map(int, input().split())
        school['Yonsei'] += a
        school['Korea'] += b
    
    if school['Yonsei'] > school['Korea']:
        print('Yonsei')
    elif school['Yonsei'] < school['Korea']:
        print('Korea')
    else:
        print('Draw')