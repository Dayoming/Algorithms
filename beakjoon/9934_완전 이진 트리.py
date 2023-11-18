import sys
input = sys.stdin.readline

k = int(input())
nodes = list(map(int, input().split()))
n = 2 ** k
tree = [0] * n # 1번 인덱스부터 시작
idx = 0

def in_order(node):
    global idx
    
    if node < n:
        in_order(node * 2) # left
        tree[node] = nodes[idx] # root
        idx += 1
        in_order(node * 2 + 1) # right

in_order(1)
idx = 1
while idx < n:
    for i in range(idx, idx * 2):
        print(tree[i], end = ' ')
    print()
    idx *= 2