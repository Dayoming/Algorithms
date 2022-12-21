# 과제 안 내신 분..?
number = [x for x in range(1, 31)]
submitN = []
result = []

for i in range(28):
    n = int(input())
    submitN.append(n)

for i in number:
    if i not in submitN:
        result.append(i)

print(min(result))
print(max(result))