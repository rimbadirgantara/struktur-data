from os import system as sy
sy('cls')
print('\nPercobaan 1 : Menciptakan class node')
# Mendefenisikan sebuah class dengan nama "node"
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
# Pengecekan tipe
print(Node)

print('\nPercobaan 2 : Menciptakan class single linked list')
# Mendefenisikan sebuah class single linked list dengan nama
"SlinkedList"
class SLinkedList:
    def __init__(self):
        self.head = None
    # Fungsi untuk menambahkan node pada posisi awal

    def tambahawal(self, data_in):
        nodebaru = Node(data_in)
        nodebaru.next = self.head
        self.head = nodebaru
    # Fungsi untuk menghapus node

    def hapusnode(self, Removekey):
        datumhead = self.head
        if (datumhead is not None):
            if (datumhead.data == Removekey):
                self.head = datumhead.next
                datumhead = None
                return
        # while (datumhead is not None):
        #     if datumhead.data == Removekey:
        #         break
        prev = datumhead
        datumhead = datumhead.next
        if (datumhead == None):
            return
        prev.next = datumhead.next
        datumhead = None

    def cetaklinkedlist(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next
# Pengecekan tipe
print(SLinkedList)

print('\nPercobaan 3 : Menciptakan objek dan mengisi datum pada elemen/node linked list')
# Menciptakan objek linked list dengan 'senarai'
senarai = SLinkedList()
# Mengisi node linked list dengan node 'senin'
senarai.tambahawal("Senin")
# Mengisi node linked list dengan node 'selasa'
senarai.tambahawal("Selasa")
# Mengisi node linked list dengan node 'rabu'
senarai.tambahawal("Rabu")
# Cetak linked list
print("\nIsi linked list")
senarai.cetaklinkedlist()

print('\nPercobaan 4 : Menghapus elemen/node linked list')
# Menghapus node
senarai.hapusnode("Selasa")
# Cetak linked list
print("\nIsi linked list setelah ada penghapusan")
senarai.cetaklinkedlist()
