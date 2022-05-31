from os import system as sy
sy('cls')

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

print('Percobaan 1: Menciptakan Node untuk tree')
print(Node)

print('\nPercobaan 2: Membuat root dari sebuah tree menggunakan class node')
root = Node(1)
print(root)
print(''' 
Ilustrasi yang akan terjadi seperti dibawah ini
    1
   / \\
None None
''')

print('\nPercobaan 3: Membuat left child dan right chile dari root')
root.left = Node(2)
root.right = Node(3)
print(root.left)
print(root.right)
print(''' 
Ilustrasi yang akan terjadi seperti dibawah ini
             1
          /     \
         2       3
       /  \    /   \
    None None None None
''')
print('\nPercobaan 4: Membuat left child dari parent "2"')
root.left.left = Node(4)
print(root.left.left)
print('\n')
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
print(root.left.right)
print(root.right.left)
print(root.left.left)
print('''Ilustrasi yang akan terjadi seperti dibawah ini
              1
          /       \\
         2        3
        / \     /   \\
       4   5   6     None
      /    \
     7    None
''')