# 하노이 탑 이동 순서

def hanoi(n, a, b, c):
    if n == 1:
        frame.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        frame.append([a, c])
        hanoi(n-1, b, a, c)

frame = []
hanoi(int(input()), 1, 2, 3)

print(len(frame))
print("\n".join([' '.join(str(i) for i in row) for row in frame]))