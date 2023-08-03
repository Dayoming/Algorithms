import sys

n = int(sys.stdin.readline())
log = {}

for _ in range(n):
    name, stat = sys.stdin.readline().split()
    if stat == "enter":
        log[name] = stat
    else:
        del log[name]

log = sorted(log.keys(), reverse=True)

for i in log:
    print(i)