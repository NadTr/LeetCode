# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None or k == 0:
            return head
        list_len = 1
        node = head
        while node.next:
            list_len += 1
            node =node.next
        node.next = head
        for i in range(list_len - (k % list_len)):
            print(node.val)
            node = node.next
        head = node.next
        node.next = None
        return head

        