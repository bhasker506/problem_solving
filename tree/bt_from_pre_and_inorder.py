# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(val=preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid], inorder[:mid])
        root.right = self.buildTree(preorder[mid:], inorder[mid:])
        return root
    

if __name__ == '__main__':
    s = Solution()
    root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])