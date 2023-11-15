import sys

n, r, c = map(int, sys.stdin.readline().split())

def many_times_visited(n, r, c):
    if n == 0:
        return 0
    
    return 2 * (r % 2) + (c % 2) + 4 * many_times_visited(n - 1, int(r/2), int(c/2))

print(many_times_visited(n, r, c))