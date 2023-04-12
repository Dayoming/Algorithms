n, m = map(int, input().split())
arr1 = set(input() for _ in range(n))
arr2 = set(input() for _ in range(m))

answer = sorted(list(arr1 & arr2))

print(len(answer))

for i in answer:
    print(i)