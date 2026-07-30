# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit_to_carry = 0
        node = ListNode()
        l = node
        
        while l1 or l2 or digit_to_carry:
            l_sum = digit_to_carry
            if l1:
                l_sum += l1.val
                l1 = l1.next
            if l2:
                l_sum += l2.val
                l2 = l2.next
            
            new_node = ListNode(l_sum % 10)
            digit_to_carry = l_sum // 10
            node.next = new_node
            node = new_node

        return l.next
