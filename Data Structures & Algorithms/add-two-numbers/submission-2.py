# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         
         l1_current = l1
         l2_current = l2
         res = ListNode(0)
         current_new = res
         carry = 0

         while l1_current is not None or l2_current is not None or carry > 0:
            l1_val = l1_current.val if l1_current is not None else 0
            l2_val = l2_current.val if l2_current is not None else 0

            total = l1_val + l2_val + carry
            carry = total // 10
            node_value = total % 10

            current_new.next = ListNode(node_value)
            current_new = current_new.next


            if l1_current is not None:
                l1_current = l1_current.next
            if l2_current is not None:
                l2_current = l2_current.next
        
         return res.next

        