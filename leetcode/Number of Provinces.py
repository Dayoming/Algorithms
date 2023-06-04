from collections import deque

class Solution(object):
    def findCircleNum(self, isConnected):
        # 방문한 주 그래프
        visited = set()
        
        # 주의 개수를 세기 위한 변수
        count = 0
        
        for i in range(len(isConnected)):
            # 방문하지 않은 주라면
            if i not in visited:
                # 방문 처리
                visited.add(i)
                queue = deque()
                queue.append(i)
                # 큐가 존재하는 동안
                while queue:
                    # 현재 위치 주
                    curr = queue.popleft()
                    # 주의 개수 만큼 [1, 1, 0, 1] <- 이면 4번
                    for neighbour in range(len(isConnected[curr])):
                        # 만약 방문하지 않은 주이고, 두 주가 연결되어 있다면
                        if neighbour not in visited and isConnected[curr][neighbour] == 1:
                            # 큐에 해당 주를 넣어주고 방문 처리
                            queue.append(neighbour)
                            visited.add(neighbour)
                count += 1
        return count                    
        

s = Solution()
print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))