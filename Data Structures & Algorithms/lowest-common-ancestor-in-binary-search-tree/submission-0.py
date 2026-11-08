# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. we need to check if p and q are both subroot of a specific root
# 2. one of the cases is that the p or q is equal to the ancestor of p or q
# 3. because this is a bst the p should be <= and q should be >= ancestor 


# pseudo:
# if both p and q are smaller than root go to left
# else if go to right
# else return root

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root