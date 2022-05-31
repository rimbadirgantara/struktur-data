from os import system as sy
sy('cls')
print('\nPercobaan 1, Menciptakan class node')
# Mendefinisikan sebuah class node
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
print(Node)

print('\nPercobaan 2, Menciptakan class singel list')
# Mendefenisikan sebuah class single linked list dengan nama "SlinkedList"
class SLinkedList:
    def __init__(self):
        self.headval = None
# Fungsi utnuk menambah node

    def inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("Node tidak tersedia")
            return
    # Menciptakan objek node dengan nama 'NewNode'
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    # Cetak linked list

    def cetaklinkedlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
# Pengece   kan tipe
print(SLinkedList)

print('\nPercobaan 3, Menciptakan objek dan mengisi datum pada elemen/node linked list')
# Menciptakan objek linked list dengan 'senarai'
senarai = SLinkedList()
# Mengisi head dari linked list dengan node 'senin'
senarai.headval = Node("Senin")
# Cek hasil isian dengan mencetak linked list
senarai.cetaklinkedlist()
# Membuat objek dari class 'node' dengan nama e2 dan e3 disertai nilai datum
e2 = Node("Selasa")
e3 = Node("Kamis")
# Merangkai node e2 dengan posisi setelah head
senarai.headval.nextval = e2
# Merangkai node e3 dengan posisi setelah node ke-2
e2.nextval = e3
# Cetak linked list
print("Isi linked list")
senarai.cetaklinkedlist()

print('\nPercobaan 4 : Menyisip elemen/node linked list diantara node')
# Menyisip node 'rabu'
senarai.inbetween(senarai.headval.nextval, "Rabu")
# Cetak linked list
print("\nIsi linked list setelah disisip")
senarai.cetaklinkedlist()
