class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.preorder_insert(self.root, new_val)

    def search(self, find_val):
        return self.preorder_search(self.root, find_val)

    def preorder_insert(self, start, new_val):
        if not start:
            start = Node(new_val)
        elif start.value >= new_val:
            self.preorder_insert(start.left, new_val)
        else:
            self.preorder_insert(start.right, new_val)

    def preorder_search(self, start, find_val):
        if start.value == find_val:
            return True
        elif start.value < find_val and start.left:
            self.preorder_search(start.left, find_val)
        elif start.value > find_val and start.right:
            self.preorder_search(start.right, find_val)
        else:
            return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
