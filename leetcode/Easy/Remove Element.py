class Solution(object):
    def removeElement(self, nums, val):
        # 새로운 리스트를 만들고 싶지 않지만 기존의 리스트를 대체하고 싶을 때,
        # 리스트 축약[:]을 사용
        nums[:] = [value for value in nums if value != val]
        
        return len(nums)

s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))