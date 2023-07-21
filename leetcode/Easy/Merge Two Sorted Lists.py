# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        head = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 if list1 is not None else list2
        
        return dummy.next

def linked_list_print(l):
    if l is None: 
        return ''
    return str(l.val)+'->'+linked_list_print(l.next)

s = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print(linked_list_print(s.mergeTwoLists(list1, list2)))

list3 = None
list4 = None

print(linked_list_print(s.mergeTwoLists(list3, list4)))

list5 = None
list6 = ListNode(0)

print(linked_list_print(s.mergeTwoLists(list5, list6)))