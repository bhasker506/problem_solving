
from typing import List


class Node:

    def __init__(self, val, left= None, right = None):
        self.val = val
        self.right = right
        self.left = left

def get_tree(arr: List) -> Node:
    if not arr:
        return
    root = Node(val=arr[0])
    convert_to_tree(arr=arr, root=root, index=0)
    return root
    

def convert_to_tree(arr: List, root: Node, index: int) -> Node:
    if index < len(arr):
        temp = Node(arr[index])
        root = temp
 
        # insert left child
        root.left = convert_to_tree(arr, root.left, 2 * index + 1)
 
        # insert right child
        root.right = convert_to_tree(arr, root.right, 2 * index + 2)
    return root

if __name__ == '__main__':
    get_tree(arr=[1, 2, 3, 4, 5, 6])