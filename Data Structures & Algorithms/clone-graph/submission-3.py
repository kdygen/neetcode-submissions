"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# 1. create a dict
# 2. for loop through all nodes : 
# 3. while node is not in dict: add it to the dict
# 4. do we want to go backwards and check what it connects to????
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict1 = {}

        def helper(node):
            if node in dict1:
                return dict1[node]
            
            copy = Node(node.val)
            dict1[node] = copy

            for i in node.neighbors:
                copy.neighbors.append(helper(i))
            return copy
        
        if node is None:
            return None
        
        return helper(node)