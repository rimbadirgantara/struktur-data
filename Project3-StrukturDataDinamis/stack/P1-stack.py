from os import system as sy
sy('cls')
# mendefinisikan sebuah class denga nama "stack"


class Stack:
    # konstruktor
    def __init__(self):
        self.tumpukan = []
    # method untuk fungsi push()

    def push(self, datum):
        # melakukan pengecekan apakah datum suda ada atau belum
        if datum not in self.tumpukan:
            # apabila belum, tambahkan ke stack
            self.tumpukan.append(datum)
            return True
        else:
            return False
    # method pop

    def pop(self):
        if len(self.tumpukan) <= 0:
            return ('tidak ada elemen di stack')
        else:
            return self.tumpukan.pop()

 # pengecek tipe
print('Percobaan 1')
print(Stack)

print('\nPercobaan 2')
# menciptakan objek stack
objek_stack = Stack()
# cek apakah stack sudah ada isi atau belum
print('kondisi awal stack')
print(objek_stack.tumpukan)
print('\nMenghitung jumlah elemen stack')
print(len(objek_stack.tumpukan))

# operasi push
print('\nOperasi push')
objek_stack.push('senin')
objek_stack.push('selasa')
objek_stack.push('rabu')
objek_stack.push('kamis')
objek_stack.push('jumat')
objek_stack.push('sabtu')
objek_stack.push('minggu')
print(objek_stack.tumpukan)

print('\nPercobaan 3')
print('Operasi pop')
objek_stack.pop()
print('Pop yang ke-1')
print(objek_stack.tumpukan)
objek_stack.pop()
print(objek_stack.tumpukan)
objek_stack.pop()
print('Pop yang ke-2')
print(objek_stack.tumpukan)
objek_stack.pop()
print('Pop yang ke-3')
print(objek_stack.tumpukan)
objek_stack.pop()
print('Pop yang ke-4')
print(objek_stack.tumpukan)
objek_stack.pop()
print('Pop yang ke-5')
print(objek_stack.tumpukan)
objek_stack.pop()
print('Pop yang ke-6')
print(objek_stack.tumpukan)
