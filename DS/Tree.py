# TREE
# 1)A tree is a hierarchical data structure.
# 2)Unlike arrays, linked lists, stacks, or queues (which are linear structures), trees represent non-linear relationships.

# binary tree
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data)
#         if self.right:
#             self.right.PrintTree()

# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(22)
# root.PrintTree()

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Preorder Traversal (Root → Left → Right)
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

# Inorder Traversal (Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Postorder Traversal (Left → Right → Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# Build Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Traversals
print("Preorder traversal of binary tree is:")
preorder(root)

print("\nInorder traversal of binary tree is:")
inorder(root)

print("\nPostorder traversal of binary tree is:")
postorder(root)













