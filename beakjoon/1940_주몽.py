import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
# 재료 배열
material = list(map(int, input().split()))
material.sort()

left = 0
right = len(material) - 1
# 만들어진 갑옷 개수
armor = 0

while left < right:
    temp = material[left] + material[right]

    if temp < m:
        left += 1
    elif temp > m:
        right -= 1
    elif temp == m:
        armor += 1
        left += 1


print(armor)
    