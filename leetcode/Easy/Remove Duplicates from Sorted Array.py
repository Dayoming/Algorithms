class Solution(object):
    def removeDuplicates(self, nums):
        # 처음 풀이
        # return len(list(set(nums)))
        # set은 요소의 순서를 저장하지 않기 때문에 틀린 답
        
        # 동일한 변수 이름으로 새 목록을 재정의하는 대신 기존 목록을 업데이트하지 않음
        nums[:] = sorted(list(set(nums)))
        return len(nums)


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))