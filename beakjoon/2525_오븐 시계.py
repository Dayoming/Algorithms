now_h, now_m = map(int, input().split())
minute = int(input())

now_m = now_m + minute
now_h = now_h + (now_m // 60)
now_m = now_m % 60

if now_h >= 24:
    now_h = now_h - 24

print(now_h, now_m)