# 당신에게 n개의 높이가 주어진다.
# 그것들은 n개의 세로 줄들인데, 두 개의 끝점이 (i, 0)과 (i, height[i])인
# 두 개의 가장 많은 물을 담을 수 있는 선을 찾아라 
# 컨테이너가 저장할 수 있는 가장 많은 물의 양을 반환해라
# 단, 컨테이너는 기울일 수 없음

class Solution(object):
    def maxArea(self, height):
        maximum = 0
        # 포인터 두 개 선언
        left = 0
        right = len(height) - 1
        
        while left < right:
            # 컨테이너의 넓이는 가로 * 세로
            temp = (right - left) * min(height[left], height[right])
            maximum = max(maximum, temp)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return maximum

solution = Solution()
print(solution.maxArea([2,3,4,5,18,17,6]))