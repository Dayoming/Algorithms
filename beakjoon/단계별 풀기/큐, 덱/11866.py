# 요세푸스 문제 0

n, k = map(int, input().split())
# 큐로 사용할 리스트 생성
queue = [i for i in range(1, n + 1)]
removed = []
now = k - 1

while queue:
    # queue에서 삭제한 값을 removed에 추가
    removed.append(queue.pop(now))
    if queue:
        # 하나 감소했으므로 1을 빼주고 k값을 더한 후 queue의 길이로 나눈 나머지
        now = ((now-1) + k) % len(queue)

print(f'<{", ".join(map(str,removed))}>')
