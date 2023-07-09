# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = ""
        
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        sum = str(int((n1)[::-1]) + int((n2)[::-1]))[::-1]
        answer = ListNode[0]
        temp = answer
        for i in sum:
            temp.next = ListNode(int(i))
            temp = temp.next
            
        return answer.next
    
s = Solution()
print(s.addTwoNumbers([2, 4, 3], [5, 6, 4]))
print(s.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))