# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        self.head, self.tail = None, None
        self.expand_tree_dfs(root)
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head
        
        
    def expand_tree(self, node):
        if not node:
            return
        
        self.expand_tree(node.left)
        if self.tail:
            self.tail.right = node
            node.left = self.tail
        else:
            self.head = node
        self.tail = node
        self.expand_tree(node.right)
    
    
    def expand_tree_dfs(self, node):
        stk = []
        
        while True:
            while node:
                stk.append(node)
                node = node.left
            
            if not stk:
                break

            element = stk.pop()
            if self.tail:
                self.tail.right = element
                element.left = self.tail
            else:
                self.head = element
            self.tail = element
            node = element.right
            

if __name__ == '__main__':
    root = Node(val=4)
    root.left = Node(val=2)
    root.right = Node(val=5)
    root.left.left = Node(val=1)
    root.left.right = Node(val=3)
    
    s = Solution()
    s.treeToDoublyList(root)