# 음계
music = list(map(int, input().split()))
asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]

if music == asc:
    print("ascending")
elif music == des:
    print("descending")
else:
    print("mixed")