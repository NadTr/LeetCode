# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def rootToLeaf(root):
            left_path = right_path = []
            if root == None:
                return None
            if not root.right and not root.left:
                return [[root.val]]
            if root.left:
                left_path = [path + [root.val] for path in rootToLeaf(root.left)]      
            if root.right:
                right_path = [path + [root.val] for path in rootToLeaf(root.right)]
            return left_path + right_path

        total = 0
        all_paths = rootToLeaf(root)
        for path in all_paths:
            total += sum(path[i]* (10**i) for i in range(len(path)))
        return total