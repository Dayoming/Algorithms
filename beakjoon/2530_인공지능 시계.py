
hour, minute, seconds = map(int, input().split())

cook_seconds = int(input())

cook_hour = cook_seconds // 3600
cook_minute = (cook_seconds // 60) % 60 # 초를 분으로 변환하고 시간으로 나눈 나머지
cook_seconds = cook_seconds % 60

hour = hour + cook_hour
minute = minute + cook_minute
seconds = seconds + cook_seconds

if seconds >= 60:
    minute = minute + (seconds // 60)
    seconds = seconds % 60

if minute >= 60:
    hour = hour + (minute // 60)
    minute = minute % 60

if hour >= 24:
    hour = hour % 24

print(hour, minute, seconds)