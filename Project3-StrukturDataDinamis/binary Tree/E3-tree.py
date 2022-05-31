from os import system as sy
sy('cls')

class Node:
    def __init__(self, data):
        self.kiri = None
        self.kanan = None
        self.nilai = data

def inorder(root):
    if root:
        inorder(root.kiri)
        print(root.nilai)
        inorder(root.kanan)
    
def postorder(root):
    if root:
        postorder(root.kiri)
        postorder(root.kanan)
        print(root.nilai)
    
def preorder(root):
    if root:
        print(root.nilai)
        preorder(root.kiri)
        preorder(root.kanan)
    

root = Node('F')
# akar kanan
root.kanan = Node('G')
root.kanan.kanan = Node('I')
root.kanan.kanan.kiri = Node('H')
#akar kiri
root.kiri = Node('B')
root.kiri.kiri = Node('A')
root.kiri.kanan = Node('D')
root.kiri.kanan.kiri = Node('C')
root.kiri.kanan.kanan = Node('E')

print('Fasilitas pre order')
preorder(root)
print('\nFasilitas in order')
inorder(root)
print('\nFasilitas post order')
postorder(root)