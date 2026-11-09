# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. we need to go to the smallest val here first
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = None

        def inOrder(node):
            nonlocal k, answer

            if not node or answer is not None:
                return
            
            inOrder(node.left)

            if answer is not None:
                return

            k -= 1

            if k == 0:
                answer = node.val
                return
            
            inOrder(node.right)
        
        inOrder(root)
        return answer



