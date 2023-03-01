# 이분 탐색
# 최장 증가 부분 수열(LIS)

N = int(input())
A = list(map(int, input().split()))
memorization = [0]

for i in A:
    if memorization[-1] < i:
        memorization.append(i)
    else:
        left = 0
        right = len(memorization)

        while left < right:
            mid = (left + right) // 2

            if memorization[mid] < i:
                left = mid + 1
            else:
                right = mid
        
        memorization[right] = i

print(len(memorization) - 1)