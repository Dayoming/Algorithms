# 문서 검색

document = input()
text = input()
result = 0
while text in document:
    result += 1
    document = document.replace(text, ' ', 1)

print(result)