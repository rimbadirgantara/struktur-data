from os import system as sy
sy('cls')
# Mendefinikan sebuah class denga nama 'Node'
print('Percobaan 1, Mengenal class node')


# ini adalah class node
class Node:
    def __init__(self, dataval=None):
        # ini adalah func untuk inisialiasasi class node
        # funct __init__ adalah konstruktor. parameter self tugas nya adalah memanggil class itu sendiri
        # dataval adalah parameter buatan sendiri(programmer), sebagai penampung data
        self.dataval = dataval  # ini sama dengan dataval_new = dataval
        self.nextval = None
        # ini sama dengan nextval = None, var ini sebagai penyambung ke node lain


# Pengecekan tipe
print(Node)

print('\nPercobaan 2, Menciptakan class singel linked list')
# mendefinisikan sebuah class singel linked list dengan nama 'SlingedList'

class SLinkedList:
    def __init__(self):
        self.headval = None

    # method cetak linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # Method insert node di awal linkedlist
    def sisipawal(self, newdata):
        newnodeawal = Node(newdata)
        # update list dengan penambahan node baru
        newnodeawal.nextval = self.headval
        self.headval = newnodeawal

print(SLinkedList)

print('\nPercobaan 3, Menciptakan objek dan mengisi datum pada elemen linked list')
# Menciptakan objek Single Linked List dengan nama 'list'
objeklist = SLinkedList()
# Mengisi datum untuk node pada posisi head linked list
objeklist.headval = Node("Senin")
# Menciptakan objek 'node' untuk elemen ke-2
e2 = Node("Selasa")
# Menciptakan objek 'node' untuk elemen ke-3
e3 = Node("Rabu")
e4 = Node('Kamis')
e5 = Node('Jumat')
# Merangkai elemen ke-2 dengan head dari linked list
objeklist.headval.nextval = e2
# Merangkai elemen ke-3 dengan elemen ke-2 dari linked list
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
# cetak single linked list
print("\nNilai elemen single linked list :")
objeklist.listprint()

print('\nPercobaan 4, Menambah elemen list di awal linked list')
# insert diawal
objeklist.sisipawal("Minggu")
# Cetak List
print("Nilai elemen single linked list setelah disisip: ")
objeklist.listprint()
