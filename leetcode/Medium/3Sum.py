from itertools import combinations

class Solution(object):
    def threeSum(self, nums):
        answer = []
        
        for i in combinations(nums, 3):
            i = sorted(list(i))
            if sum(i) == 0 and i not in answer:
                answer.append(i)
        return answer

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))