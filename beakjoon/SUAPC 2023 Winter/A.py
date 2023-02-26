# A번 - 카트라이더: 드리프트
records = []
score = [10, 8, 6, 5, 4, 3, 2, 1, 0]
red, blue = 0, 0

for i in range(8):
    record = input()
    records.append(record)

records.sort()

for i in range(len(records)):
    record, team = records[i].split()
    if team == 'R':
        red += score[i]
    elif team == 'B':
        blue += score[i]

if red > blue:
    print('Red')
else:
    print('Blue')