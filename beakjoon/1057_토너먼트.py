n, jimin, hansu = map(int, input().split())

num1 = jimin
num2 = hansu
star_round = 1

while True:
    if num2 - num1 == 1 and num2 % 2 == 0:  # If num1 and num2 is sequential number, break
        break
    else:
        if num1 % 2 == 1:  # If num1 is odd, next number / 2
            num1 = (num1 + 1) / 2
        else:
            num1 = num1 / 2  # If num1 is even,
        if num2 % 2 == 1:  # If num2 id odd, next number / 2
            num2 = (num2 + 1) / 2
        else:
            num2 = num2 / 2
        star_round += 1  # round increase

print(star_round)
