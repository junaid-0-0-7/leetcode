# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0) #for the starting point of linkedlist which is 0
        end = start         #for the moving point of linkedlist which will change n+1
        carry = 0
        while l1 or l2 or carry:
           val1 = l1.val if l1 else 0
           val2 = l2.val if l2 else 0

           total = val1 + val2 + carry

           digit = total % 10     #for getting the last number like 4 from 104
           carry = total // 10    #for removing the last number and getting rest like 10 from 104
           
           end.next = ListNode(digit) #creating the next end node
           end = end.next             #assigning the next end point

           if l1:
            l1 = l1.next
           if l2:
            l2 = l2.next


        return start.next