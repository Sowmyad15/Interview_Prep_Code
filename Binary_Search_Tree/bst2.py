class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.key:
        root.left=insert(root.left,key)
    elif key>root.key:
        root.right=insert(root.right,key)
    return root

def inorder(root):
    if root is None:
        return -1
    else:
        inorder(root.left)
        print(str(root.key)+"->",end=" ")
        inorder(root.right)

def preorder(root):
    if root is None:
        return -1
    else:
        print(str(root.key)+"->",end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root is None:
        return -1
    else:
        postorder(root.left)
        postorder(root.right)
        print(str(root.key)+"->",end=" ")

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("Preorder traversal: ", end=' ')
preorder(root)

print("Postorder traversal: ", end=' ')
postorder(root)
