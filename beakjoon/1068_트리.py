import sys

# 깊이 우선 탐색을 통해 탐색
def dfs(num, arr):
    # 전달 받은 노드 값을 삭제한다 -> -2로 바꾼다.
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

# 노드의 개수 n
n = int(sys.stdin.readline())
# 각 노드의 부모. 부모가 없다면 -1
arr = list(map(int, sys.stdin.readline().split()))
# 지울 노드의 번호
k = int(sys.stdin.readline())
# 리프 노드의 개수를 저장할 변수 count
count = 0

dfs(k, arr)

for i in range(len(arr)):
    # 삭제된 노드가 아니고 i값이 arr에 존재하지 않으면
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)