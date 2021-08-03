from tree.binaray_tree import Node


class TreeTraversals:

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val)
            self.inorder_traversal(root.right)
        return

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val)

    def preorder_traversal(self, root):
        if root:
            print(root.val)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def level_order_traversal(self, root):
        if not root:
            return
        queue = []
        queue.append(root)

        while queue:
            n = queue.pop(0)
            print(n.val)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    traversals = TreeTraversals()
    # traversals.inorder_traversal(root=root)
    # traversals.preorder_traversal(root=root)
    # traversals.postorder_traversal(root=root)
    traversals.level_order_traversal(root=root)