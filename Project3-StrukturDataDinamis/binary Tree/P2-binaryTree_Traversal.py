from os import system as sy
sy('cls')

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
print('Percobaan 1: Menciptakan node untuk tree')
print(Node)

def printInorder(root):
    if root:
        #rekursif untuk left child
        printInorder(root.left)
        # nilai node
        print(f'{root.val}')
        #rekursif untuk right child
        printInorder(root.right)
    
def printPostorder(root):
    if root:
        # rekursif untuk left child
        printPostorder(root.left)
        # rekursif untuk right child
        printPostorder(root.right)
        # nilai dari node
        print(root.val)

def printPreorder(root):
    if root:
        # nilai dari node
        print(root.val)
        # rekursif untuk left child
        printPreorder(root.left)
        # rekursif untuk right child
        printPreorder(root.right)
root = Node(1)
print('\nPercobaan 2: Membuat method inorder')
print('\nPercobaan 3: Membuat method postorder')
print('\nPercobaan 4: Membuat method preorder')
print('\nPercobaan 5: Menciptakan tree')

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("""
                  1
                /   \\
               2     3
              / \       
             4   5
""")

print('\nPercobaan 6: Menjalankan penelusuran (transversal) tree')
print('Inorder traversal dari binary tree :')
printInorder(root)
print('\nPostorder traversal dari binary tree :')
printPostorder(root)
print('\nPreorder traversal dari binary tree :')
printPreorder(root)
