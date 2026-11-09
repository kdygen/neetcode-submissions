# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1.  if root.left.val < root.val and root.right.val > root.val- true 
# 2.  else false
# 3. 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lower, upper):
            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            left = validate(node.left, lower, node.val)
            right = validate(node.right, node.val, upper)
            return left and right
        return validate(root, float('-inf'), float('inf'))