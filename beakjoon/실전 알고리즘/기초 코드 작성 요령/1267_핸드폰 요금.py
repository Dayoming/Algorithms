n = int(input())
times = list(map(int, input().split()))

# 영식 요금제는 30초마다 10원, 민식 요금제는 60초마다 15원
youngsik = 0
minsik = 0

for i in times:
    youngsik += i // 30 * 10 + 10
    minsik += i // 60 * 15 + 15

if youngsik < minsik:
    print('Y', youngsik)
elif minsik < youngsik:
    print('M', minsik)
else:
    print('Y M', youngsik)