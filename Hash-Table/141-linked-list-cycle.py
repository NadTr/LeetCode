# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_visited = set()
        while head and head not in node_visited:
            node_visited.add(head)
            head = head.next
        return head in node_visited