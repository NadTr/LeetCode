# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_visited = set()

        while headA and headA not in node_visited :
            node_visited.add(headA)
            headA = headA.next

        while headB and headB not in node_visited: 
            headB = headB.next

        return headB