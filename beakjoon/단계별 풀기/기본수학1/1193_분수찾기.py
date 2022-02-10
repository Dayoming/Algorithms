x = int(input())
line = 0
end = 0

while x > end:
    line += 1
    end += line

diff = end - x
if line % 2 == 0:
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print(top, bottom, sep='/')