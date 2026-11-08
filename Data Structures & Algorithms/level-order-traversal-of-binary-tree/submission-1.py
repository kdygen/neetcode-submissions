# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. create a list
# 2. create a queue with root 
# 3. while queue we should create a level [] and level size(queue)
# 4. for loop with range of level size
# 5. now we extract the node of it and append that to level
# 6. and we have to update our queue with left and right nodes so it keeps going

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level = []
            levelSize = len(queue)

            for i in range(levelSize):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                
            result.append(level)
        return result



