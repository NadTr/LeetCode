# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return None

        node = head
        slow_node = head
        fast_node = head
        while fast_node and fast_node.next:
            node = slow_node
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        node.next = node.next.next if node.next.next else None

        return head

        