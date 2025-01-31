class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val, node):
        if self.root is None:  # If tree is empty, set root
            self.root = Node(val)
            return self.root

        if node is None: # this is our main base case 
            return Node(val)

        if val < node.data: # lesser val left side 
            node.left = self.insert(val, node.left)
        else: # greater or equal val rifght side 
            node.right = self.insert(val, node.right)

        return node

    def inorder(self, node):

        if node is None:
            return []
        return self.inorder(node.left) + [node.data] + self.inorder(node.right)

# Main Function
if __name__ == "__main__":
    bst = BST()
    values = [10, 5, 15, 3, 7, 12, 18]
    for v in values:
        bst.insert(v, bst.root)

    print("Inorder Traversal of BST:")
    print(bst.inorder(bst.root))
