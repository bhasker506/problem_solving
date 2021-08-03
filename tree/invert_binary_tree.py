# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:

# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:

# Input: root = []
# Output: []


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.right = left
        root.left = right
        
        return root

if __name__ == '__main__':
    root = TreeNode(val=4)
    root.left = TreeNode(val=2)
    root.left.left = TreeNode(val=1)
    root.left.right = TreeNode(val=3)
    
    root.right = TreeNode(val=7)
    root.right.left = TreeNode(val=6)
    root.right.right = TreeNode(val=9)
    
    s = Solution(root=root)