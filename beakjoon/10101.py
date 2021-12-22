# 삼각형 외우기

angle = []
sum_angle = 0
result = ''

for i in range(3):
    angle.append(int(input()))

for i in angle:
    sum_angle = sum_angle + i

if sum_angle != 180:
    result = 'Error'
else:
    angle = set(angle)

    if len(angle) == 3:
        result = 'Scalene'
    elif len(angle) == 2:
        result = 'Isosceles'
    elif len(angle) == 1:
        result = 'Equilateral'

print(result)