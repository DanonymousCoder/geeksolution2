
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
    
class Solution:
    def maxDepth(self,root):
        pass
    
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
