# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        node = head
        while node and node.next:
            node2 = node.next
            node3 = node.next.next
            
            node2.next = head
            head = node2
            node.next = node3

        return head