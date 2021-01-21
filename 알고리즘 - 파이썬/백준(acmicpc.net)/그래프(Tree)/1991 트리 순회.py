import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(root):
    print(root.data, end = "")
    if root.left != '.':
        preorder(tree[root.left])
    if root.right != '.':
        preorder(tree[root.right])

def inorder(root):
    if root.left != '.':
        inorder(tree[root.left])
    print(root.data, end = "")
    if root.right != '.':
        inorder(tree[root.right])

def postorder(root):
    if root.left != '.':
        postorder(tree[root.left])
    if root.right != '.':
        postorder(tree[root.right])
    print(root.data, end = "")

n = int(input())
tree = {}
for i in range(n):
    data, left, right = input().strip().split()
    tree[data] = Node(data, left, right)
    
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])


