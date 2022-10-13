# 배열을 하나 만든 다음에 map으로 연산자, 값을 구분하고
# 연산자에 따라서 값을 넣어주고, 뺴주면 될 것 같은데..?

def solution(operations):
    queue = []
    for i in range(len(operations)):
        # 연산자와 값 구분해서 저장하기
        operation, value = map(str, operations[i].split())
        # 데이터 삽입
        if operation == 'I':
            queue.append(int(value))
        elif operation == 'D':
            # 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우 무시
            if len(queue) == 0:
                continue
            if int(value) == 1:
                queue.remove(max(queue))
            elif int(value) == -1:
                queue.remove(min(queue))
    # 큐가 비어있으면 [0, 0]을, 비어있지 않으면 [최댓값, 최솟값] 반환
    if len(queue) == 0:
        return [0, 0]
    else:
        return [max(queue), min(queue)]


print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
