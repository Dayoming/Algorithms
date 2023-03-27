import sys

string = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())
cursor = len(string)

for _ in range(m):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif command[0] == 'D':
        if cursor != (len(string) - 1):
            cursor += 1
    elif command[0] == 'B':
        if cursor != 0:
            del string[cursor - 1]
            cursor -= 1
    elif command[0] == 'P':
        string.insert(cursor, command[1])
        cursor += 1

print(''.join(string))